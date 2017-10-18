import glob
import re
import json
import codecs

files=glob.glob('./charsets/index-*.txt')
titlePattern=re.compile("-[^\.]+")

for fname in files:
    with open(fname,encoding='utf8') as f:
        title=titlePattern.findall(fname)[0][1:]
        print("Generating table for " + title)
        lookupTable={}
        for line in f:
            try:
                code=int(line.split("\t")[0]) #just to skip wrong lines
                chunk=line.split("x")[1].split("\t")
                code=chunk[0]
                char=chunk[1].split(" ")[0]
                lookupTable[code]=char
            except:
                pass
        with open(title+'.json', 'w', encoding='utf8') as json_file:
            data = json.dumps(lookupTable, ensure_ascii=False,indent=4)
            json_file.write(str(data))
    