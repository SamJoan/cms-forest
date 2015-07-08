from os.path import join
from os import listdir
from os import listdir
from os.path import isdir, join, isfile
import hashlib

def md5(f):
    m = hashlib.md5()
    with open(f) as fh:
        m.update(fh.read())

    return m.hexdigest()

directories = [ f for f in listdir(".") if isdir(join(".",f)) ]
with open('interesting_files.txt') as f:
    for line in f:
        url = line.strip()
        print('\t<file url="'+url+'">')
        for d in directories:
            fpath = join(d, url)
            hsh = md5(fpath)

            print('\t\t<version md5="'+hsh+'" nb="'+d+'" />')

        print("\t</file>")
