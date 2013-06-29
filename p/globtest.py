# coding:cp932

import glob

files = glob.glob('nippou_*.txt')
for f in files:
  print "ファイル:%s" % f

