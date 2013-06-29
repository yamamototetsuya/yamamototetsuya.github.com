# coding:cp932

# 貸出冊数を集計する（まず全行）
count = 0
f = open('bjournal.txt')
for line in f:
  count = count + 1

print "データの行数は，%d行でした。" % count

