name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for lines in handle:
    if lines.startswith('From '):
        lst = lines.split()
        d[lst[1]] = d.get(lst[1], 0) + 1

max_value = None
mail = None
for k,v in d.items():
    if mail is None or max_value < v:
        mail = k
        max_value = v
        
print(mail, max_value)