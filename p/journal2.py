# coding:cp932


# �����Ƃ̑ݏo�������W�v����i�ꉞ�����j
mfreq = {}
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  k = d[0][0:7]
  # �W�v�p�����ɃL�[���Ȃ���΁C�����l��0�����Ă���
  if k not in mfreq:
    mfreq[k] = 0
  # �ЂƂ��W�v
  mfreq[k] += 1

# ���|�[�g�\��
ks = mfreq.keys()
ks.sort()
for k in ks:
  print "%s �݂̑��o������: %d" % (k, mfreq[k])

