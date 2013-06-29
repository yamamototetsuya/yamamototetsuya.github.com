# coding:cp932

# 分類ごとの貸出冊数を集計する・特殊ルール適用版
cfreq = {}
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  # 分類の類目だけを取り出す
  k = d[2][:1]
  # ルール1: Xは読み飛ばし
  if k == 'X':
    continue
  # ルール2: Sならば2文字目を改めて取り出す
  if k == 'S':
    k = d[2][1:2]
  # ルール3: Aは実は9
  if k == 'A':
    k = '9'
  # 集計用辞書にキーがなければ，初期値の0を入れておく
  if k not in cfreq:
    cfreq[k] = 0
  # ひとつずつ集計
  cfreq[k] += 1

# レポート表示
ks = cfreq.keys()
ks.sort()
for k in ks:
  print "分類 %s の貸し出し冊数: %d" % (k, cfreq[k])

