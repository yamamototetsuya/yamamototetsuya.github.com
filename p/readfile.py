f = open('data.txt')
for i in f:
  print "line:"
  print i[:-1]
f.close()

