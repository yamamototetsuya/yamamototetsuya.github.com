# coding:cp932

import os
os.linesep = '\r\n'

# ���E�������Ƃ̋��z���W�v����
kin = {}
f = open('kingaku.txt')
for line in f:
  d = line[:-1].split("\t")
  print d
  # ���ɂ����镔�������o��
  k = d[0][:7]
  # ����ɕ����R�[�h���������āC�L�[�ɂ���
  k = k + " " + d[1]
  # �W�v�p�����ɃL�[���Ȃ���΁C�����l��0�����Ă���
  if k not in kin:
    kin[k] = 0
  # ���z�𑫂�����
  if d[2].isdigit():
    kin[k] += int(d[2])

# ���|�[�g�\��
print kin
ks = kin.keys()
ks.sort()
for k in ks:
  k2 = k.split(" ")
  print "%s �̕���%s�̍w���z: %d" % (k2[0], k2[1], kin[k])

