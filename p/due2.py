# coding:cp932

# 注: このスクリプトは実行してもエラーを起こします

import datetime

# n日後を算出（ただし休館日は計算に入れない）
def calc_days_after_without_closeday(from_d, n):
  d = from_d
  c = n
  while 1:
    if c == 0:
      break
    d = d + datetime.timedelta(1)
    if [dが休館日なら]:
      continue
    c -= 1
  return d

