#!/usr/bin/env python3
"""G207: add native source preservation, Finder BDF and modern xFontMedic fixtures
fixtures. Original compressed font members must be bit-preserved. Archive
replaced root metadata in the designated historical-files folder.
"""
from pathlib import Path,PurePosixPath
import io,json,hashlib,plistlib,struct,zlib,zipfile,re,sys,tempfile
from fontTools.ttLib import TTFont

OLD=Path("xFontGauntlet_v2.15.zip")
NEW=Path("xFontGauntlet_v2.15.zip")
OLD_HASH="219fed0da2923ba7510fdd4e9d4c93d2687c42181ac51f1b723ef7f2c22ddf29"
GROUP="205_G207_Finder_BDF_Converter_Native_Auditor_New_Validations"
P="TestCorpus/"+GROUP+"/"
ARCHIVE="Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G207_Post_v2_14_Coverage/"
META=("CURRENT_CORPUS_MANIFEST.json","CORPUS_COVERAGE_LOCK.json","CORPUS_CATALOG.json")
TTF="TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/02_Metadata_And_Actual_Content/Baseline.ttf"
WOFF2="TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/04_FontMedic_Audit_Repair/Valid_WOFF2/ValidBrotli.woff2"
UFO="TestCorpus/196_Recent_X01_X04_Regression_Cases_20261013/01_Renamer_Directory_Backed/ToRename/Opaque_Source.ufo/"
entries={}
cases=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def filehash(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for block in iter(lambda:f.read(1048576),b""):h.update(block)
    return h.hexdigest()
def jsonb(obj):return (json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+"\n").encode("utf-8")
def write(name,data):
    path=P+name
    assert isinstance(data,bytes) and path not in entries
    entries[path]=data
    return name
def case(project,fixture,scenario,expected,tags=(),kind="fixture"):
    i=len(cases)+1
    cases.append(dict(id=f"G207-{i:03d}",projects=[project],fixture=fixture,
                      scenario=scenario,expected=expected,tags=list(tags),kind=kind))
def make_ttf(seed,name,change=0):
    with TTFont(io.BytesIO(seed),recalcBBoxes=True,recalcTimestamp=False) as f:
        for n in (1,4,16):f["name"].setName(name,n,3,1,1033)
        if change:
            glyph=f["glyf"]["A"]
            glyph.coordinates[0]=(glyph.coordinates[0][0]+change,glyph.coordinates[0][1])
        b=io.BytesIO();f.save(b);r=b.getvalue()
    with TTFont(io.BytesIO(r)) as chk:
        assert "name" in chk and "glyf" in chk
    return r
def treehash(records):
    h=hashlib.sha256()
    for row in sorted(records,key=lambda r:r["path"]):
        h.update((row["path"]+"\0"+str(row["size_bytes"])+"\0"+row["sha256"].lower()+"\n").encode())
    return h.hexdigest()
def directories(names):
    result=set()
    for name in names:
        if name.endswith("/"):result.add(name)
        for p in PurePosixPath(name.rstrip("/")).parents:
            if str(p)==".":break
            result.add(str(p)+"/")
    return sorted(x for x in result if x.startswith("TestCorpus/"))
def assert_fixture_structure(old):
    # All three repaired G200 UFO3 packages must survive entirely unchanged.
    for p in (
        UFO,
        "TestCorpus/196_Recent_X01_X04_Regression_Cases_20261013/07_Cross_Tool_Folder_Atomics/Finder_Copied_Set.ufo/",
        "TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/01_Rename_248_Boundary/Input/NestedFinderSet.ufo/"
    ):
        assert plistlib.loads(old.read(p+"layercontents.plist"))==[["public.default","glyphs"]]

from g207_fixture_cases import populate

def build_cases(original):
    return populate(original,write,case,entries,P,sha,jsonb,make_ttf,TTF,cases)

def build():
    assert OLD.is_file() and OLD.stat().st_size==98807621 and filehash(OLD)==OLD_HASH, "Incorrect full v2.14 baseline"
    assert not NEW.exists(), "Refuse to overwrite any existing v2.15"
    with zipfile.ZipFile(OLD) as original:
        old_info=original.infolist()
        old_names=[i.filename for i in old_info]
        assert len(old_info)==54048 and len(set(old_names))==54048
        assert original.testzip() is None
        assert all(x in old_names for x in META)
        assert all(x not in old_names for x in entries)
        new_manifest=build_cases(original)
        assert len(new_manifest["cases"])==31
        # Create deterministic full TestCorpus manifest/lock over physically
        # present files. Root metadata and Tools archive are not corpus fixtures.
        active={}
        for info in old_info:
            n=info.filename
            if info.is_dir() or not n.startswith("TestCorpus/"):continue
            data=original.read(info)
            active[n]={"path":n,"size_bytes":len(data),"sha256":sha(data)}
        for n,b in entries.items():
            if not n.startswith("TestCorpus/") or b is None:continue
            assert n not in active,n
            active[n]={"path":n,"size_bytes":len(b),"sha256":sha(b)}
        records=sorted(active.values(),key=lambda x:x["path"])
        dirs=directories([x for x in old_names if x.startswith("TestCorpus/")]+list(entries))
        tree=treehash(records)
        source_manifest=json.loads(original.read(META[0]))
        source_lock=json.loads(original.read(META[1]))
        catalog=json.loads(original.read(META[2]))
        source_manifest.update({
            "created_date":"2026-10-14",
            "title":"xFontGauntlet 2.15 Current Corpus Integrity Manifest",
            "scope":"Active TestCorpus/ only; 20 root metadata files and Tools/ are excluded",
            "excluded_paths":[],
            "baseline_zip_sha256":OLD_HASH,
            "file_count":len(records),
            "directory_count":len(dirs),
            "tree_sha256":tree,
            "files":records,"directories":dirs,
            "repair_notes":{"group":GROUP,"source_release":"v2.14",
                "original_records_archived":ARCHIVE+"Originals/"},
        })
        source_manifest.setdefault("release_identity",{}).update({
            "version":"2.15","display_name":"xFontGauntlet 2.15",
            "release_filename":"xFontGauntlet_v2.15.zip",
            "source_lineage":"G207 appended to authoritative v2.14 G206 full corpus"})
        source_lock.update({
            "created_date":"2026-10-14",
            "purpose":"Current G207 coverage lock refreshed, prior record retained in archive.",
            "current_lock_scope":"All active TestCorpus/ files and directories; excludes Tools and root metadata.",
            "locked_file_count":len(records),
            "locked_directory_count":len(dirs),
            "locked_tree_sha256":tree,
            "files":records,"directories":dirs,
            "repair_notes":{"group":GROUP,"original_records_archived":ARCHIVE+"Originals/"},
        })
        existing_groups=catalog.get("groups",[])
        assert isinstance(existing_groups,list)
        assert not any(x.get("group")==205 for x in existing_groups)
        subfiles=[x for x in records if x["path"].startswith(P)]
        subdirs=[x for x in dirs if x.startswith(P)]
        existing_groups.append({
            "group":205,"folder":GROUP,
            "coverage_area":"Recent_x01_x04_Regression_Coverage",
            "file_entries":len(subfiles),
            "directory_entries":len(subdirs),
            "content_bytes":sum(x["size_bytes"] for x in subfiles),
            "root_manifest_records":0,
            "declared_logical_cases":31,
            "declared_case_source":P+"EXPECTED_RESULTS.json",
            "expected_result_files":[P+"EXPECTED_RESULTS.json"]})
        for area in catalog.get("coverage_areas",[]):
            if isinstance(area,dict) and area.get("id")=="Recent_x01_x04_Regression_Coverage":
                ids=area.setdefault("groups",[])
                if isinstance(ids,list) and 205 not in ids:ids.append(205)
        catalog["groups"].sort(key=lambda x:x["group"])
        catalog["created_date"]="2026-10-13"
        catalog["title"]="xFontGauntlet 2.15 Comprehensive Corpus Catalog"
        accounting=catalog.setdefault("accounting",{})
        accounting["groups"]=205
        accounting["declared_logical_cases"]=2969
        catalog.setdefault("release_identity",{}).update({
            "version":"2.15","display_name":"xFontGauntlet 2.15",
            "release_filename":"xFontGauntlet_v2.15.zip",
            "source_lineage":"G207 append to authoritative v2.14"})
        # v2.11 stores a second current release identity in the coverage lock.
        current_release=source_lock.get("current_release")
        if isinstance(current_release,dict):
            current_release["version"]="2.15"
            for key in ("release_filename","archive_filename"):
                if key in current_release:current_release[key]="xFontGauntlet_v2.15.zip"
        catalog["g207_coverage_review"]={"x01":"Earlier metadata probe coverage preserved","x02":"Native TTF/OTF/TTC/OTC bypass and strict existing-output checks","x03":"Byte-exact actual corrupted BDF false-confirmed regression inputs","x04":"BDF GLIF AFM PFB CSS SVG large SFD and Glyphs audit regressions","declared_case_count":31}
        changes={META[0]:jsonb(source_manifest),META[1]:jsonb(source_lock),META[2]:jsonb(catalog)}
        for name in META:
            entries[ARCHIVE+"Originals/"+name]=original.read(name)
        entries[ARCHIVE+"CHANGE_LOG.json"]=jsonb({
            "source_release":"v2.14","source_zip_sha256":OLD_HASH,
            "new_group":GROUP,"declared_case_count":31,
            "changed_metadata":[{"path":name,"old_sha256":sha(original.read(name)),"new_sha256":sha(changes[name]),
              "original_archive":ARCHIVE+"Originals/"+name} for name in META],
            "old_fixture_files_changed":0,"group_13_unchanged":True,
            "runtime_assertions":"NOT_EXECUTED"
        })
        entries[ARCHIVE+"BUILD_VALIDATION.json"]=jsonb({
            "result":"PENDING_FINAL_FULL_ZIP_AUDIT",
            "scope":"G207 static fixtures, archived metadata originals and preserved prior corpus members",
            "legacy_python_powershell_validators":"Not treated as passed (inherited five failures in v2.8)"
        })
        assert all(n not in old_names for n in entries)
        assert set(changes)==set(META)
        # The raw ZIP writer below retains all original compressed bytes and
        # metadata, modifying only the three listed root metadata files.
        # Add only new G207 entries and archived metadata files.
        # New archive directories only. Existing directories and every original
        # font fixture's local compressed bytes remain unchanged.
        new_dirs=set()
        for n in entries:
            if n.endswith("/") and n not in old_names:new_dirs.add(n)
            for p in PurePosixPath(n).parents:
                if str(p)==".":break
                d=str(p)+"/"
                if d not in old_names:new_dirs.add(d)
        with io.BytesIO() as mem:
            with zipfile.ZipFile(mem,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as add:
                for n in sorted(new_dirs,key=lambda x:(x.count("/"),x)):
                    i=zipfile.ZipInfo(n,date_time=(2026,10,13,20,0,0))
                    i.external_attr=(0o40755<<16)|0x10
                    add.writestr(i,b"")
                for n,b in sorted(entries.items()):
                    if b is None:continue
                    i=zipfile.ZipInfo(n,date_time=(2026,10,13,17,0,0))
                    i.external_attr=(0o100644<<16)
                    i.compress_type=zipfile.ZIP_DEFLATED
                    add.writestr(i,b,compresslevel=9)
            addzip=mem.getvalue()

        # Original local payloads are retained bit-for-bit except changed metadata;
        # updated metadata uses method-preserving local headers; new entries use
        # the addendum's local+central records.
        raw=OLD.read_bytes()
        with zipfile.ZipFile(io.BytesIO(addzip)) as addon:
            added_info=addon.infolist()
            assert len(set(x.filename for x in added_info))==len(added_info)
            assert not set(old_names).intersection(x.filename for x in added_info)
            assert addon.testzip() is None
            order=sorted(enumerate(old_info),key=lambda x:x[1].header_offset)
            new_offsets={}
            edits={}
            parts=[raw[:order[0][1].header_offset]]
            position=len(parts[0])
            for pos,(index,info) in enumerate(order):
                a=info.header_offset
                b=order[pos+1][1].header_offset if pos+1<len(order) else original.start_dir
                segment=raw[a:b]
                assert segment[:4]==b"PK\x03\x04"
                if info.filename in changes:
                    assert info.flag_bits&8==0 and info.compress_type in (0,8),info.filename
                    name_len,extra_len=struct.unpack_from("<HH",segment,26)
                    offset=30+name_len+extra_len
                    assert offset+info.compress_size==len(segment),info.filename
                    content=changes[info.filename]
                    if info.compress_type==8:
                        co=zlib.compressobj(9,zlib.DEFLATED,-15)
                        packed=co.compress(content)+co.flush()
                    else:packed=content
                    crc=zlib.crc32(content)&0xffffffff
                    head=bytearray(segment[:offset])
                    struct.pack_into("<III",head,14,crc,len(packed),len(content))
                    segment=bytes(head)+packed
                    edits[index]=(crc,len(packed),len(content))
                new_offsets[index]=position
                parts.append(segment)
                position+=len(segment)
            # Append new local entries from prepared ZIP, retaining byte content
            addon_order=sorted(enumerate(added_info),key=lambda x:x[1].header_offset)
            for pos,(index,info) in enumerate(addon_order):
                a=info.header_offset
                b=addon_order[pos+1][1].header_offset if pos+1<len(addon_order) else addon.start_dir
                seg=addzip[a:b]
                assert seg[:4]==b"PK\x03\x04"
                new_offsets[len(old_info)+index]=position
                parts.append(seg)
                position+=len(seg)
            central_offset=position
            def copy_central(blob,start,infos,offset_index,edited):
                nonlocal position
                cursor=start
                for index,info in enumerate(infos):
                    assert blob[cursor:cursor+4]==b"PK\x01\x02"
                    nl,el,cl=struct.unpack_from("<HHH",blob,cursor+28)
                    end=cursor+46+nl+el+cl
                    record=bytearray(blob[cursor:end])
                    assert struct.unpack_from("<I",record,42)[0]==info.header_offset
                    struct.pack_into("<I",record,42,new_offsets[offset_index+index])
                    if index in edited:struct.pack_into("<III",record,16,*edited[index])
                    parts.append(record);position+=len(record);cursor=end
                return cursor
            end_old=copy_central(raw,original.start_dir,old_info,0,edits)
            end_add=copy_central(addzip,addon.start_dir,added_info,len(old_info),{})
            eocd_old=raw.rfind(b"PK\x05\x06")
            eocd_add=addzip.rfind(b"PK\x05\x06")
            assert eocd_old==end_old and eocd_add==end_add
            eocd=bytearray(raw[eocd_old:])
            assert len(eocd)==22+struct.unpack_from("<H",eocd,20)[0]
            assert len(old_info)+len(added_info)<65535
            assert position-central_offset<0xffffffff and central_offset<0xffffffff
            struct.pack_into("<HH",eocd,8,len(old_info)+len(added_info),len(old_info)+len(added_info))
            struct.pack_into("<II",eocd,12,position-central_offset,central_offset)
            parts.append(eocd)
            NEW.write_bytes(b"".join(parts))

            try:
                with zipfile.ZipFile(NEW) as result:
                    full=result.infolist()
                    assert len(full)==len(old_info)+len(added_info)
                    assert len(set(i.filename for i in full))==len(full)
                    assert result.testzip() is None
                    assert original.comment==result.comment
                    root0=sorted(i.filename for i in old_info if "/" not in i.filename)
                    root1=sorted(i.filename for i in full if "/" not in i.filename)
                    assert root0==root1 and len(root0)==20
                    fields=("CRC","file_size","compress_size","compress_type","date_time",
                            "flag_bits","extra","comment","external_attr","internal_attr","create_system")
                    changed_count=0
                    for before,after in zip(old_info,full):
                        assert before.filename==after.filename
                        if before.filename in changes:
                            changed_count+=1
                            assert result.read(after)==changes[before.filename]
                            assert result.read(ARCHIVE+"Originals/"+before.filename)==original.read(before)
                        else:
                            for f in fields:
                                assert getattr(before,f)==getattr(after,f),(before.filename,f)
                            if not before.is_dir():
                                with original.open(before) as a,result.open(after) as b:
                                    h1=hashlib.sha256();h2=hashlib.sha256()
                                    while True:
                                        x=a.read(1048576);y=b.read(1048576)
                                        assert len(x)==len(y),before.filename
                                        if not x:break
                                        h1.update(x);h2.update(y)
                                    assert h1.digest()==h2.digest(),before.filename
                    assert changed_count==3
                    for n,b in entries.items():
                        if b is not None:assert result.read(n)==b,n
                    # No G200 repaired fixture changes, including the required layercontents.
                    for prefix in (UFO,
                        "TestCorpus/196_Recent_X01_X04_Regression_Cases_20261013/07_Cross_Tool_Folder_Atomics/Finder_Copied_Set.ufo/",
                        "TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/01_Rename_248_Boundary/Input/NestedFinderSet.ufo/"):
                        assert result.read(prefix+"layercontents.plist")==original.read(prefix+"layercontents.plist")
                    group13=[i for i in old_info if re.search(r"(^|/)13_[^/]+/",i.filename)]
                    assert len(group13)==22109
                    for i in group13:
                        j=result.getinfo(i.filename)
                        assert i.CRC==j.CRC and i.file_size==j.file_size and i.compress_size==j.compress_size
                    # Every physical active file is accounted for by the regenerated lock.
                    m=json.loads(result.read(META[0]))
                    lock=json.loads(result.read(META[1]))
                    assert m["file_count"]==lock["locked_file_count"]==len(records)
                    assert m["directory_count"]==lock["locked_directory_count"]==len(dirs)
                    assert m["tree_sha256"]==lock["locked_tree_sha256"]==tree
                    mapping={r["path"]:r for r in m["files"]}
                    assert len(mapping)==len(records)
                    for name,data in entries.items():
                        if name.startswith(P) and data is not None:
                            assert mapping[name]["sha256"]==sha(data)
                    manifest=json.loads(result.read(P+"EXPECTED_RESULTS.json"))
                    assert manifest["declared_case_count"]==31 and len(manifest["cases"])==31
                    assert sum("x01" in c["projects"] for c in manifest["cases"])==0
                    assert sum("x02" in c["projects"] for c in manifest["cases"])==6
                    assert sum("x04" in c["projects"] for c in manifest["cases"])==21
                    for path,h in manifest["fixture_hashes"].items():
                        assert sha(result.read(path))==h,path
                    assert len({c["id"] for c in manifest["cases"]})==31
                    for c in manifest["cases"]:
                        fullpath=P+c["fixture"].rstrip("/")
                        assert any(n.startswith(fullpath) for n in result.namelist()),c["id"]
                    print("VERIFICATION RESULT: PASS",
                          json.dumps({"previous_entries":len(old_info),"new_entries":len(added_info),
                                      "new_cases":31,"active_files":len(records),
                                      "group13_original_entries":len(group13),
                                      "unchanged_previous_font_fixtures":True,
                                      "modified_root_metadata":3,
                                      "archive_size":NEW.stat().st_size},sort_keys=True))
            except:
                NEW.unlink(missing_ok=True)
                raise
    output_hash=filehash(NEW)
    Path("xFontGauntlet_v2.15.zip.sha256").write_text(output_hash+"  xFontGauntlet_v2.15.zip\n",encoding="ascii")
    print("FULL_ZIP_SHA256",output_hash)

if __name__=="__main__":
    try:build()
    except Exception as e:
        print("VERIFICATION RESULT: FAIL",repr(e),file=sys.stderr)
        raise
