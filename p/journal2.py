# coding:cp932


# 月ごとの貸出冊数を集計する（一応完成）
mfreq = {}
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  k = d[0][0:7]
  # 集計用辞書にキーがなければ，初期値の0を入れておく
  if k not in mfreq:
    mfreq[k] = 0
  # ひとつずつ集計
  mfreq[k] += 1

# レポート表示
ks = mfreq.keys()
ks.sort()
for k in ks:
  print "%s の貸し出し冊数: %d" % (k, mfreq[k])

