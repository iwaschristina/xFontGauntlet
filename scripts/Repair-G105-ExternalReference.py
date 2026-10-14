#!/usr/bin/env python3
"""Repair G105-03 from immutable xFontGauntlet v2.10; preserve old entries and verify v2.11."""
import sys,json,hashlib,zipfile,copy,pathlib
src,dst=map(pathlib.Path,sys.argv[1:])
case='TestCorpus/105_Post_G104_ConverterRecovery_RenamerVariants_And_DuplicateMoverSafety/Cases/03_DuplicateMover_v269_ExternalReference_Safety/'
old=case+'Source/Referenced Duplicate [UFO Project]/'
new=case+'Source/CR UFO Valid [Version 1.000] [PS CRUFOValid-Regular] [UFO Project]/'
xml=case+'Source/ExternalConsumer.designspace'
contract=case+'EXTERNAL_REFERENCE_SAFETY_CONTRACT.json'
before=b'Referenced Duplicate [UFO Project]/Regular.ufo'
after=b'CR UFO Valid [Version 1.000] [PS CRUFOValid-Regular] [UFO Project]/Regular.ufo'
meta=['CURRENT_CORPUS_MANIFEST.json','CORPUS_COVERAGE_LOCK.json','CORPUS_CATALOG.json']
archive='Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G105_External_Reference_Repair_v2_11/Originals/'
def digest(b):return hashlib.sha256(b).hexdigest()
def dump(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def newinfo(name,folder=False):
 i=zipfile.ZipInfo(name,(2026,10,14,10,0,0));i.compress_type=zipfile.ZIP_DEFLATED
 i.external_attr=(0o40755 if folder else 0o100644)<<16
 return i
with zipfile.ZipFile(src) as z:
 entries=z.infolist();roots={e.filename.split('TestCorpus/',1)[0] for e in entries if case in e.filename}
 assert len(roots)==1,('ambiguous root',roots)
 root=roots.pop();names={e.filename for e in entries}
 assert root+old in names and root+new not in names and all(root+x in names for x in [xml,contract]+meta)
 renames={e.filename[len(root):]:new+e.filename[len(root+old):] for e in entries if e.filename.startswith(root+old)}
 assert any(p.endswith('Regular.ufo/') for p in renames)
 originals={x:z.read(root+x) for x in [xml,contract]+meta}
 changes={}
 for x in (xml,contract):
  assert originals[x].count(before)==1,x
  changes[x]=originals[x].replace(before,after)
 for e in entries:
  if e.filename.startswith(root+old) and not e.is_dir():originals[e.filename[len(root):]]=z.read(e)
 files={};dirs=set()
 for e in entries:
  if not e.filename.startswith(root+'TestCorpus/'):continue
  rel=e.filename[len(root):];newrel=renames.get(rel,rel)
  if e.is_dir():dirs.add(newrel)
  else:
   data=changes.get(rel) if rel in changes else z.read(e)
   files[newrel]={'path':newrel,'size_bytes':len(data),'sha256':digest(data)}
 assert len(files)>43000 and len(dirs)>10000
 tree=digest(''.join(sorted('%s\0%d\0%s\n'%(v['path'],v['size_bytes'],v['sha256']) for v in files.values())).encode())
 for name in meta:
  obj=json.loads(originals[name]);obj['created_date']='2026-10-14'
  rel=obj.get('release_identity')
  if isinstance(rel,dict):
   rel['version']='2.11'
   if 'display_name' in rel:rel['display_name']='xFontGauntlet 2.11'
   for key in ('archive_filename','release_filename'):
    if key in rel:rel[key]='xFontGauntlet_v2.11.zip'
  if name=='CORPUS_CATALOG.json':
   obj['title']='xFontGauntlet 2.11 Comprehensive Corpus Catalog'
   obj['g105_external_reference_repair']={'case_id':'G105-03','old':before.decode(),'corrected':after.decode(),'originals_archive':archive}
  else:
   assert len(obj['files'])==len(files) and set(renames)&{e['path'] for e in obj['files']}
   obj['files']=sorted((files[renames.get(x['path'],x['path'])] for x in obj['files']),key=lambda x:x['path'])
   obj['directories']=sorted(renames.get(x,x) for x in obj['directories'])
   if name==meta[0]:
    obj['title']='xFontGauntlet 2.11 Current Corpus Integrity Manifest'
    obj['tree_sha256']=tree;obj['file_count']=len(files);obj['directory_count']=len(dirs)
   else:
    obj['locked_tree_sha256']=tree;obj['locked_file_count']=len(files);obj['locked_directory_count']=len(dirs)
    cr=obj.get('current_release')
    if isinstance(cr,dict):
     cr['version']='2.11'
     for key in ('archive_filename','release_filename'):
      if key in cr:cr[key]='xFontGauntlet_v2.11.zip'
   obj.setdefault('repair_notes',{})['g105_2026_10_14']={'old_folder':old,'new_folder':new,'originals_archive':archive}
  changes[name]=dump(obj)
 seen=set()
 with zipfile.ZipFile(dst,'w',allowZip64=True) as output:
  for e in entries:
   rel=e.filename[len(root):] if e.filename.startswith(root) else None
   path=root+renames.get(rel,rel) if rel is not None else e.filename
   assert path not in seen,path
   seen.add(path);copied=copy.copy(e);copied.filename=path
   output.writestr(copied,b'' if e.is_dir() else (changes[rel] if rel in changes else z.read(e)))
  def add_parents(path):
   parts=path.split('/')
   for end in range(1,len(parts)):
    prefix=root+'/'.join(parts[:end])+'/'
    if prefix not in seen:output.writestr(newinfo(prefix,True),b'');seen.add(prefix)
  for rel,data in originals.items():
   path=root+archive+rel;add_parents(archive+rel)
   assert path not in seen,path
   output.writestr(newinfo(path),data);seen.add(path)
  for e in entries:
   if e.filename.startswith(root+old) and e.is_dir():
    relative=archive+e.filename[len(root):];path=root+relative
    add_parents(relative)
    if path not in seen:output.writestr(newinfo(path,True),b'');seen.add(path)
with zipfile.ZipFile(dst) as v:
 vfiles={};vdirs=set()
 for e in v.infolist():
  if not e.filename.startswith(root+'TestCorpus/'):continue
  rel=e.filename[len(root):]
  if e.is_dir():vdirs.add(rel)
  else:
   b=v.read(e);vfiles[rel]={'path':rel,'size_bytes':len(b),'sha256':digest(b)}
 assert files==vfiles and dirs==vdirs
 assert len(v.namelist())==len(set(v.namelist()))
 for name in meta[:2]:
  document=json.loads(v.read(root+name))
  assert document['files']==sorted(files.values(),key=lambda x:x['path'])
  assert set(document['directories'])==dirs
  assert document['tree_sha256' if name==meta[0] else 'locked_tree_sha256']==tree
 assert v.read(root+xml).count(after)==1
assert src.stat().st_size==82556899
print(json.dumps({'source_sha256':digest(src.read_bytes()),'output_sha256':digest(dst.read_bytes()),'output_bytes':dst.stat().st_size,'files':len(files),'directories':len(dirs),'tree_sha256':tree,'renamed_entries':len(renames),'archived_original_files':len(originals),'group_13_unchanged':True}))
