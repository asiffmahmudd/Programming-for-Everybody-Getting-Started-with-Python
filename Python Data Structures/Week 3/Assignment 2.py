# Use the file name file2.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
a = 0;
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    count += 1
    x = float(line[19:].lstrip())
    a += x

avg = a/count    
print("Average spam confidence:", avg)