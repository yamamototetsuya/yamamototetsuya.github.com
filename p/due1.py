# coding: cp932

import datetime

# 返却期限の関数を作成中（友の会と夏休みキャンペーンを考慮）
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
  d = out_date + datetime.timedelta(period)
  return d

# 実際に使ってみる
a = datetime.date(2012, 4, 1)
print calc_due_date(a, 0)
print calc_due_date(a, 1)
a = datetime.date(2012, 8, 1)
print calc_due_date(a, 0)
print calc_due_date(a, 1)
