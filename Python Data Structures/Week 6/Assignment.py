name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst1 = list()
lst2 = list()
d = dict()
for line in handle:
    if line.startswith('From '):
        lst1 = line.split()
        lst2 = lst1[5].split(':')
        d[lst2[0]] = d.get(lst2[0], 0) + 1

lst = list()
lst = sorted(d.items())
for k, v in lst:
    print(k,v)

