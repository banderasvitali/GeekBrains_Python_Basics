from os import walk, getcwd, stat, path
from collections import defaultdict

d = defaultdict(int)
for paths, dirs, files in walk(getcwd()):
    for i in files:
        x = len(str(stat(path.join(paths, i)).st_size))
        d[10**x] += 1

print(dict(sorted(d.items(), key=lambda x: x[0])))
    
