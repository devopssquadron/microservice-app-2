
# Logs input file

file = open('hello.txt')
count = 0
for line in file:
    if ('p') in line:
        print (line)
        count = count + 1
print (count)
