# coding: cp932

import datetime

# �ԋp�����̊֐����쐬���i�F�̉�Ɖċx�݃L�����y�[�����l���j
def calc_due_date(out_date, tomo):
  # �F�̉�
  if tomo == 1:
    period = 28
  else:
    # �ċx��
    if out_date.month == 8:
      period = 28
    else:
      period = 14
  d = out_date + datetime.timedelta(period)
  return d

# ���ۂɎg���Ă݂�
a = datetime.date(2012, 4, 1)
print calc_due_date(a, 0)
print calc_due_date(a, 1)
a = datetime.date(2012, 8, 1)
print calc_due_date(a, 0)
print calc_due_date(a, 1)
