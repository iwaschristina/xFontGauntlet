"""Archive historical Group 13 without making routine TestCorpus extraction slow.

The inner ZIP contains the exact Group 13 directory tree, relative to TestCorpus/.
Its bytes and file metadata are checked against the immutable authoritative ZIP.
"""
import io,hashlib,re,zipfile

GROUP_FOLDER = "13_Corruption_Matrix_All_Font_Types"
SOURCE_PREFIX = "TestCorpus/" + GROUP_FOLDER + "/"
OPTIONAL_ZIP = "Tools/Optional Test Groups/Group13_Corruption_Matrix_All_Font_Types.zip"
OPTIONAL_GUIDE = "Tools/Optional Test Groups/README_Group13.txt"

def group13_members(old):
    infos=[x for x in old.infolist() if x.filename.startswith(SOURCE_PREFIX)]
    assert len(infos)==21633,("Group13 membership changed",len(infos))
    assert any(i.is_dir() for i in infos) and any(not i.is_dir() for i in infos)
    return infos

def build_optional_group13(old,infos):
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,"w",allowZip64=False) as out:
        for info in infos:
            relative=info.filename[len("TestCorpus/"):]
            assert relative.startswith(GROUP_FOLDER+"/")
            zi=zipfile.ZipInfo(relative,info.date_time)
            zi.compress_type=info.compress_type
            zi.create_system=info.create_system
            zi.external_attr=info.external_attr
            zi.internal_attr=info.internal_attr
            zi.comment=info.comment
            # New deterministic ZIP container, original member bytes preserved.
            out.writestr(zi,b"" if info.is_dir() else old.read(info),compress_type=zi.compress_type,compresslevel=6)
    result=buf.getvalue()
    with zipfile.ZipFile(io.BytesIO(result)) as z:
        after=z.infolist()
        assert len(after)==len(infos)
        assert z.testzip() is None
        assert all(a.filename==b.filename[len("TestCorpus/"):] for a,b in zip(after,infos))
        for a,b in zip(after,infos):
            assert (a.is_dir(),a.file_size,a.CRC,a.external_attr,a.date_time)==(b.is_dir(),b.file_size,b.CRC,b.external_attr,b.date_time),b.filename
            if not b.is_dir():
                h1=hashlib.sha256()
                h2=hashlib.sha256()
                with old.open(b) as s,z.open(a) as d:
                    while True:
                        p=s.read(1024*1024);q=d.read(1024*1024)
                        assert len(p)==len(q)
                        if not p:break
                        h1.update(p);h2.update(q)
                assert h1.digest()==h2.digest(),b.filename
    return result
