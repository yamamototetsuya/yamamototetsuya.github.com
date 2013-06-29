# coding: cp932

import datetime

# 今日の日付（設定できるようにした）
today_d = datetime.date(2012, 7, 12)

# 休館日情報を読み込む
closeday = []
for line in open('closeday.txt'):
  a = line[:-1].split("/")
  d = datetime.date(int(a[0]), int(a[1]),
                        int(a[2]))
  closeday.append(d)

# n日後を算出（ただし休館日は計算に入れない）
def calc_days_after_without_closeday(from_d, n):
  d = from_d
  c = n
  while 1:
    if c == 0:
      break
    d = d + datetime.timedelta(1)
    if d in closeday:
      continue
    c -= 1
  return d

# 返却期限を出す関数
def calc_due_date(out_date, tomo):
  # 友の会
  if tomo == 1:
    period = 28
  else:
    # 夏休み
    if out_date.month == 8:
      period = 28
    else:
      period = 14
  d = calc_days_after_without_closeday(out_date,
         period)
  return d

# データを読み込みながら，延滞かを判定
for line in open('lending.txt'):
  a = line[:-1].split("\t")
  dd = a[2].split("/")
  dd2 = datetime.date(int(dd[0]),
                          int(dd[1]), int(dd[2]))
  due_d = calc_due_date(dd2, int(a[1]))
  if today_d > due_d:
    print "利用者 %s は，資料 %s の返却期限 %s を延滞しています。" % (a[0], a[3], due_d)
  # 期限前日のリストにしたいとき
  #delta = (due_d - today_d).days
  #if delta == 1:
  #  print "利用者 %s は，資料 %s の返却期限 %s の期限一日前です。" % (a[0], a[3], due_d)


