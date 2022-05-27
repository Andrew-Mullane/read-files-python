fhand = open('daffodils.txt')
print(fhand)


#fhand = open('bad-file.txt')
#print(fhand)
s = '1 2\t 3\n 4'
print(s)
print(repr(s))



fhand = open('daffodils.txt')
count = 0
for line in fhand:
  count = count + 1
print('Line Count:', count)

fhand = open('daffodils.txt')
for line in fhand:
  #line = line.rstrip()
  #if line.startswith('From:'):
  print(repr(line)) # works
  print(line, end = ' ')#works




fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print('There were', count, 'subject lines in', fname)