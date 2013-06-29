from urllib import urlopen
for line in urlopen('http://www.w3c.org/'):
  print line

