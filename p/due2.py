# coding:cp932

# ��: ���̃X�N���v�g�͎��s���Ă��G���[���N�����܂�

import datetime

# n������Z�o�i�������x�ٓ��͌v�Z�ɓ���Ȃ��j
def calc_days_after_without_closeday(from_d, n):
  d = from_d
  c = n
  while 1:
    if c == 0:
      break
    d = d + datetime.timedelta(1)
    if [d���x�ٓ��Ȃ�]:
      continue
    c -= 1
  return d

