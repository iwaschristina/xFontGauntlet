"""G207: physical cross-tool regression cases from newest x02/x03/x04 runs."""
import io,json,struct,zipfile,plistlib,xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont,TTCollection

def populate(old,write,case,entries,prefix,sha,jsonb,make_ttf,seed_path,cases):
    seed=old.read(seed_path)
    with TTFont(io.BytesIO(seed)) as f:assert "name" in f
    # x02: content-based conversion and strict native source-preservation.
    x2="01_X02_Native_Font_Preservation_And_Output_Safety/"
    def choose(ext,predicate):
        names=[i for i in old.infolist() if not i.is_dir() and i.filename.lower().endswith(ext)
               and 500<i.file_size<200000 and "/13_" not in i.filename]
        names.sort(key=lambda i:(i.file_size,i.filename))
        for info in names:
            binary=old.read(info)
            try:
                if predicate(binary):return info.filename,binary
            except Exception:pass
        raise AssertionError("No valid source of type "+ext)
    def sfnt(data,kind):
        with TTFont(io.BytesIO(data)) as f:
            return f.sfntVersion==(kind if isinstance(kind,str) else kind.decode("ascii")) and "name" in f
    native=[("TTF",seed_path,seed)]
    a,b=choose(".otf",lambda d:sfnt(d,"OTTO"));native.append(("OTF",a,b))
    def coll(data):
        with TTCollection(io.BytesIO(data),lazy=False) as c:
            return len(c.fonts)>=1 and all("name" in f for f in c.fonts)
    for ext in (".ttc",".otc"):
        p,d=choose(ext,coll);native.append((ext[1:].upper(),p,d))
    for fmt,oldname,data in native:
        ext="."+fmt.lower()
        dst=write(x2+"Native_"+fmt+ext,data)
        scenario=write(x2+"Native_"+fmt+".expected.json",jsonb({
          "source":dst,"original_fixture":oldname,"format":fmt,
          "source_sha256":sha(data),"expected_status":"BYPASSED",
          "byte_preservation":True,"no_generated_duplicate":True,
          "collections_preserve_faces":fmt in ("TTC","OTC"),
          "never_run_fontforge_on_valid_native":True,"version":"xFontMorph v2.17"}))
        case("x02",scenario,"Valid native "+fmt+" source passes structural checks.",
             "BYPASSED; source SHA unchanged; no converted copy, collection faces intact.",
             ("native-font","bypass","v2.17"),"scenario")
    ttx_file,ttx=choose(".ttx",lambda b:b'<' in b[:128] and b'>' in b[:128])
    disguised=write(x2+"TTX_XML_Mislabeled.ttf",ttx)
    contract=write(x2+"TTX_XML_Mislabeled.expected.json",jsonb({
       "source":disguised,"original_ttx":ttx_file,
       "source_sha256":sha(ttx),"expected":"Route by TTX XML content to converter, not native TTF bypass."}))
    case("x02",contract,"TTX XML named with .ttf extension, not a native binary SFNT.",
         "Preserve content-based TTX conversion route; never report native BYPASSED solely by extension.",
         ("ttx","content-routing","v2.17"),"scenario")
    dup=write(x2+"ExistingGeneratedOutput.ttf",seed)
    changed=write(x2+"ExistingDifferentOutput.ttf",make_ttf(seed,"G207 Different Output",change=19))
    skip=write(x2+"Existing_Output_Verification.json",jsonb({
       "candidate":dup,"candidate_sha256":sha(seed),
       "mismatched_existing":changed,
       "expected_matching":"SKIPPED only when comprehensive output validation succeeds AND output is semantically/source-derived equivalent",
       "expected_mismatched":"Never SKIPPED, preserve differing output, report conflict; no overwrite",
       "invalid_existing":"Reject malformed checksum, empty glyphs or corrupt directory rather than treating existence as success"}))
    case("x02",skip,"Valid existing output versus structurally valid but source-different existing file.",
         "Only verified equivalent output is SKIPPED; mismatching output is a conflict and must not be overwritten.",
         ("output-skip","checksum","v2.17"),"scenario")
    assert len(cases)==6

    # x03: copy three real Group13 corruption cases into a *runnable* standalone
    # group without modifying or depending on routine processing of Group13.
    x3="02_X03_BDF_Corruption_Detection_CrossTool/"
    bdfbase="TestCorpus/13_Corruption_Matrix_All_Font_Types/Bitmap-Console/bdf/"
    observed=["Entire_Content_Duplicated.bdf","Entire_Content_Triplicated.bdf","Inserted_NUL_16_Middle.bdf"]
    source_records=[]
    valid_src="TestCorpus/01_Valid_By_Extension/bdf/Valid_Native.bdf"
    valid=write(x3+"Valid_Native.bdf",old.read(valid_src))
    case("x03",valid,"Known valid BDF counterexample paired with real observed corrupt BDF copies.",
         "Recognize/copy as confirmed when dependencies and normal Finder eligibility permit.",
         ("finder","bdf","positive"))
    for filename in observed:
        original=bdfbase+filename
        data=old.read(original)
        target=write(x3+filename,data)
        source_records.append({"copied":target,"group13_original":original,"sha256":sha(data)})
        case("x03",target,"Exact BDF corruption observed falsely marked Confirmed/copied in xFontHound v2.1: "+filename,
             "Reject or flag incomplete/corrupt; never copy as Confirmed, and retain diagnostic reason.",
             ("finder","bdf","corrupt","observed-run"))
    write(x3+"SOURCE_LINEAGE_AND_RUN_CONTRACT.json",jsonb({
       "source":"Latest xFontHound 2.1 Finder run, three confirmed false-positive corrupt BDFs",
       "copies":source_records,
       "group13_unchanged":True,
       "run_mode":"Runnable without Group13 in standalone batch; compare outputs/diagnostics",
       "expected":"No corrupted BDF is labeled Confirmed/copied"}))
    assert len(cases)==10

    # x04: audit semantics from v2.0.18-2.0.37 Windows Smoke.ps1.
    x4="03_X04_Recent_Physical_Validation_Boundaries/"
    vb=old.read(valid_src)
    bdf=[
       ("Valid.bdf",vb,"VALID"),
       ("Nameless.bdf",vb.replace(b"STARTCHAR A",b"STARTCHAR"),"CORRUPT"),
       ("Reversed.bdf",vb.replace(b"STARTCHAR A",b"ENDCHAR\nSTARTCHAR A",1),"CORRUPT"),
       ("Nested.bdf",vb.replace(b"STARTCHAR A",b"STARTCHAR A\nSTARTCHAR B",1),"CORRUPT")]
    for name,data,expect in bdf:
        path=write(x4+"BDF/"+name,data)
        case("x04",path,"BDF character-block structure "+name,
             expect+"; ensure glyph name and ordered nonnested STARTCHAR/ENDCHAR.",
             ("auditor","bdf","v2.0.36"))

    ufo="TestCorpus/196_Recent_X01_X04_Regression_Cases_20261013/01_Renamer_Directory_Backed/ToRename/Opaque_Source.ufo/"
    orig={i.filename[len(ufo):]:old.read(i) for i in old.infolist() if i.filename.startswith(ufo) and not i.is_dir()}
    assert all(k in orig for k in ("metainfo.plist","fontinfo.plist","layercontents.plist","glyphs/contents.plist","glyphs/A.glif"))
    cm=plistlib.loads(orig["glyphs/contents.plist"])
    for name,mode in (("GLIF_Name_Mismatch","mismatch"),("GLIF_Missing_Format","noformat"),("GLIF_Uppercase_XML_Root","uppercase")):
        files=dict(orig)
        key,nextfile=next(iter(cm.items()))
        xml=ET.fromstring(files["glyphs/"+nextfile])
        if mode=="mismatch":xml.set("name",key+"Unexpected")
        elif mode=="noformat":xml.attrib.pop("format",None)
        else:xml.tag="GLYPH"
        files["glyphs/"+nextfile]=ET.tostring(xml,encoding="utf-8",xml_declaration=True)
        base=x4+"UFO/"+name+".ufo/"
        for rel,data in sorted(files.items()):write(base+rel,data)
        case("x04",base+"glyphs/"+nextfile,"UFO3 GLIF mapping or case-sensitive root: "+name,
             "CORRUPT; reject inconsistent glyph identity, missing format attribute, or uppercase XML root.",
             ("ufo3","glif","v2.0.37"))
    for name,data,expect in (
      ("ClassicMac_CR_Valid.afm",b"StartFontMetrics 4.1\rFontName Legacy\rEndFontMetrics\r","VALID"),
      ("ClassicMac_CR_Valid.amfm",b"StartMasterFontMetrics 4.1\rFontName Master\rEndMasterFontMetrics\r","VALID"),
      ("ClassicMac_CR_MissingEnd.afm",b"StartFontMetrics 4.1\rFontName Broken\r","CORRUPT")):
        path=write(x4+"AFM_AMFM/"+name,data)
        case("x04",path,"Classic-Mac CR-only AFM/AMFM boundaries "+name,
             expect+"; honor CR-only record ends and require closing font metrics marker.",
             ("afm","amfm","mac-cr","v2.0.34"))
    for name,data,status in (
       ("Valid_PFB.pfb",bytes((128,1,4,0,0,0,37,33,80,83,128,3)),"VALID"),
       ("Binary_First.pfb",bytes((128,2,4,0,0,0,1,2,3,4,128,3)),"CORRUPT")):
        path=write(x4+"PFB/"+name,data)
        case("x04",path,"PFB first segment must be ASCII header: "+name,
             status+"; reject binary-first PFB and preserve valid ASCII-first control.",
             ("pfb","v2.0.31"))
    for name,data,references in (
       ("Commented.css",b'/* @import "missing.css"; url("absent.woff") */ body{color:black}',[]),
       ("Active.css",b'@import "present.css"; body{color:black}',["present.css"]),
       ("QuotedCommentMarker.css",b'@import "folder/*keep*/.css";',["folder/*keep*/.css"])):
        path=write(x4+"CSS/"+name,data)
        write(x4+"CSS/"+name+".expected.json",jsonb({"source":path,"dependencies":references,"status":"VALID"}))
        case("x04",path,"CSS dependency parsing with block comments and quoted literal separators: "+name,
             "VALID; dependencies="+",".join(references)+"; no commented phantom dependencies.",
             ("css","dependencies","v2.0.28"))
    write(x4+"CSS/present.css",b"body{color:black}")
    svgbase=b'<svg xmlns="http://www.w3.org/2000/svg">'
    svgfont=b'<defs><font id="Font"><font-face font-family="Demo" units-per-em="1000"/><glyph unicode="A" d="M0 0"/></font></defs></svg>'
    for name,data,expected in (
       ("Commented.svg",svgbase+b'<!-- <image href="ghost.png"/> url(ghost.ttf) -->'+svgfont,[]),
       ("Active.svg",svgbase+b'<image href="asset.png"/>'+svgfont,["asset.png"])):
        path=write(x4+"SVG/"+name,data)
        write(x4+"SVG/"+name+".expected.json",jsonb({"source":path,"dependencies":expected,"status":"VALID"}))
        case("x04",path,"SVG XML comment and dependency extraction "+name,
             "VALID; only active linked resources appear, no ghost.png/ghost.ttf dependencies.",
             ("svg","comments","v2.0.30"))
    nl=b"\n"
    padding=(b"Comment: "+b"X"*1024+nl)*2200
    header=b"SplineFontDB: 3.0\nFontName: LargeFont\nBeginChars: 256 1\n"
    for name,ending,expected in (("Large_Valid.sfd",b"EndChars\nEndSplineFont\n","VALID_WITH_WARNINGS"),
                                 ("Large_MissingEnd.sfd",b"EndChars\n","CORRUPT")):
        path=write(x4+"LargeSFD/"+name,header+padding+ending)
        case("x04",path,"SFD terminator beyond 2MiB streaming prefix: "+name,
             expected+"; fully scan late tail and do not treat a truncated prefix as the whole source.",
             ("sfd","streaming","v2.0.35"))
    ghead=b'{\nformatVersion = 3;\nfamilyName = "LargeFont";\nfontMaster = ();\nglyphs = ();\n'
    gpad=(b"// "+b"X"*1024+b"\n")*2200
    for name,ending,expected in (("Large_Valid.glyphs",b"}\n","VALID_WITH_WARNINGS"),
                                 ("Large_MissingEnd.glyphs",b"","CORRUPT")):
        path=write(x4+"LargeGlyphs/"+name,ghead+gpad+ending)
        case("x04",path,"Glyphs closing brace beyond 2MiB source prefix: "+name,
             expected+"; stream full source and enforce balanced closing delimiter.",
             ("glyphs","streaming","v2.0.37"))
    assert len(cases)==31 and [sum(k in item["projects"] for item in cases) for k in ("x01","x02","x03","x04")]==[0,6,4,21]
    manifest={"schema":"xFontGauntlet-G207-v1","group":"205_G207_Finder_BDF_Converter_Native_Auditor_New_Validations",
      "declared_case_count":len(cases),"cases":cases,
      "fixture_hashes":{name:sha(blob) for name,blob in entries.items() if name.startswith(prefix) and blob is not None},
      "source_versions":{"x01":"xFontIdentity v2.14 (unchanged)","x02":"xFontMorph v2.17",
         "x03":"xFontHound v2.1 observed-run","x04":"xFontMedic v2.0.37"},
      "constraints":["Do not mutate prior fixtures","Retain positive versus negative expectations","Group13 unchanged and excluded from routine x02 testing"],
      "runtime_status":"NOT_EXECUTED","notes":"BDF originals are copied byte-identically out of Group13 for routine Finder validation; native source bypass is distinct from converted output."}
    write("EXPECTED_RESULTS.json",jsonb(manifest))
    write("README_G207.txt",b"G207: 31 cases x02=6, x03=4, x04=21. Includes byte-identical G13 corrupt BDF copies for routine xFontHound runs, xFontMorph native preservation, xFontMedic BDF/GLIF/PFB/AFM/CSS/SVG/SFD/Glyphs boundaries. Original corpus and Group13 untouched. Windows execution NOT_EXECUTED.\n")
    return manifest
