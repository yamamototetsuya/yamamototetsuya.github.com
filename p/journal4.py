# coding:cp932

# ���ނ��Ƃ̑ݏo�������W�v����E���ꃋ�[���K�p��
cfreq = {}
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  # ���ނ̗ޖڂ��������o��
  k = d[2][:1]
  # ���[��1: X�͓ǂݔ�΂�
  if k == 'X':
    continue
  # ���[��2: S�Ȃ��2�����ڂ����߂Ď��o��
  if k == 'S':
    k = d[2][1:2]
  # ���[��3: A�͎���9
  if k == 'A':
    k = '9'
  # �W�v�p�����ɃL�[���Ȃ���΁C�����l��0�����Ă���
  if k not in cfreq:
    cfreq[k] = 0
  # �ЂƂ��W�v
  cfreq[k] += 1

# ���|�[�g�\��
ks = cfreq.keys()
ks.sort()
for k in ks:
  print "���� %s �݂̑��o������: %d" % (k, cfreq[k])

