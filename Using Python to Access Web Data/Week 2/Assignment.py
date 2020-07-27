import re

file_handler = open('file.txt')

sum = 0
for lines in file_handler:
    line = re.findall('[\d]+', lines)
    if len(line) > 0:
        for num in line:
            sum += int(num)
print(sum)