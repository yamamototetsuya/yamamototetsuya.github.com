# coding: cp932

import datetime

# �����̓��t�i�ݒ�ł���悤�ɂ����j
today_d = datetime.date(2012, 7, 12)

# �x�ٓ�����ǂݍ���
closeday = []
for line in open('closeday.txt'):
  a = line[:-1].split("/")
  d = datetime.date(int(a[0]), int(a[1]),
                        int(a[2]))
  closeday.append(d)

# n������Z�o�i�������x�ٓ��͌v�Z�ɓ���Ȃ��j
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

# �ԋp�������o���֐�
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
  d = calc_days_after_without_closeday(out_date,
         period)
  return d

# �f�[�^��ǂݍ��݂Ȃ���C���؂��𔻒�
for line in open('lending.txt'):
  a = line[:-1].split("\t")
  dd = a[2].split("/")
  dd2 = datetime.date(int(dd[0]),
                          int(dd[1]), int(dd[2]))
  due_d = calc_due_date(dd2, int(a[1]))
  if today_d > due_d:
    print "���p�� %s �́C���� %s �̕ԋp���� %s �����؂��Ă��܂��B" % (a[0], a[3], due_d)
  # �����O���̃��X�g�ɂ������Ƃ�
  #delta = (due_d - today_d).days
  #if delta == 1:
  #  print "���p�� %s �́C���� %s �̕ԋp���� %s �̊�������O�ł��B" % (a[0], a[3], due_d)


