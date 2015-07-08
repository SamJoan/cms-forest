from collections import Counter
from os import listdir
from os.path import isdir, join, isfile
import filecmp
import hashlib
import pprint
import sys

dir_one = sys.argv[1]
dir_two = sys.argv[2]

good_extensions = ['css', 'js', 'txt']

def dircmp_recurse(dir_one, dir_two):
    comparison = filecmp.dircmp(dir_one, dir_two)
    common_files = []
    for common in comparison.common_dirs:
        common_files += dircmp_recurse(join(dir_one, common), join(dir_two, common))

    for common in comparison.common_files:
        common_files.append(join(dir_one, common))

    return common_files

def md5(f):
    m = hashlib.md5()
    with open(f) as fh:
        m.update(fh.read())

    return m.hexdigest()

def bigger_than_n(common, top_n):
    pos = 0
    for n in top_n:
        pass

    return pos

common_files = dircmp_recurse(dir_one, dir_two)
common_good = []
for common in common_files:
    extension = common.split('.')[-1]
    if extension in good_extensions:
        common_good.append(common)

directories = [ f for f in listdir(".") if isdir(join(".",f)) ]
hashes = {}
common_good_score = Counter()
should_discard = Counter()
for common in common_good:
    without_dir = "/".join(common.split("/")[1:])
    for d in directories:

        fpath = join(d, without_dir)
        if isfile(fpath):
            hsh = md5(fpath)
            if without_dir not in hashes:
                hashes[without_dir] = []

            if hsh not in hashes[without_dir]:
                hashes[without_dir].append(hsh)
                common_good_score[without_dir] += 1

        else:
            print(d)
            should_discard[without_dir] += 1

most_common = common_good_score.most_common(10)
most_discard = should_discard.most_common(5)

print(most_common)
print(most_discard)

