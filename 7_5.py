from os import walk, getcwd, stat, path
from collections import defaultdict
from json import dump

d = defaultdict(list)
for paths, dirs, files in walk(getcwd()):
    for i in files:
        x = len(str(stat(path.join(paths, i)).st_size))
        if d[10**x] == []:
            d[10**x].insert(0, 1)
        else:
            d[10 ** x][0] += 1
        if len(d[10**x]) > 1:
            if '.' in i:
                d[10 ** x][1].add(i.split('.', maxsplit=1)[1])
        else:
            if '.' in i:
                d[10 ** x].insert(1, {i.rsplit('.', maxsplit=1)[1]})

for k in d:
    d[k][1] = list(d[k][1])

d_sort = dict(sorted(d.items(), key=lambda x: x[0]))
with open(path.basename(getcwd()) + '_summary.json', 'w') as f:
    dump(d_sort, f)
