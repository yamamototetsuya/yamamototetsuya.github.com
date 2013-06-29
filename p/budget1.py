# coding:cp932

# 月・部署ごとの金額を集計する
kin = {}
f = open('kingaku.txt')
for line in f:
  d = line[:-1].split("\t")
  # 月にあたる部分を取り出す
  k = d[0][:7]
  # これに部署コードもくっつけて，キーにする
  k = k + " " + d[1]
  # 集計用辞書にキーがなければ，初期値の0を入れておく
  if k not in kin:
    kin[k] = 0
  # 金額を足しこむ
  if d[2].isdigit():
    kin[k] += int(d[2])

# レポート表示
#ks = kin.keys()
#ks.sort()
#for k in ks:
#  k2 = k.split(" ")
#  print "%s の部署%sの購入額: %d" % (k2[0], k2[1], kin[k])

# レポート出力・タブ区切り
outfile = open("report.txt", "w")
ks = kin.keys()
ks.sort()
for k in ks:
  k2 = k.split(" ")
  print >>outfile, "%s\t%s\t%s" % (k2[0], k2[1], kin[k])
outfile.close()

