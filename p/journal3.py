# coding:cp932

# 月ごとの貸出冊数を集計する（ブレイク条件を利用して）
current_month = ''
current_freq = 0
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  k = d[0][0:7]
  # ブレイクが起こった？
  if k != current_month:
    if current_freq > 0:
      print "%s の貸し出し冊数: %d" % (current_month,
                                       current_freq)
    # 注視している月とカウンタのリセット
    current_month = k
    current_freq = 0
  current_freq += 1

if current_freq > 0:
  print "%s の貸し出し冊数: %d" % (current_month,
                                   current_freq)

