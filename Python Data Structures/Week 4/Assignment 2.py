#Use file2.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for mail in fh:
    if mail.startswith('From '):
        count += 1
        lst = mail.split()
        print(lst[1])

print('There were', count, 'lines in the file with From as the first word')