# coding:cp932

# ���E�������Ƃ̋��z���W�v����
kin = {}
f = open('kingaku.txt')
for line in f:
  d = line[:-1].split("\t")
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
#ks = kin.keys()
#ks.sort()
#for k in ks:
#  k2 = k.split(" ")
#  print "%s �̕���%s�̍w���z: %d" % (k2[0], k2[1], kin[k])

# ���|�[�g�o�́E�^�u��؂�
outfile = open("report.txt", "w")
ks = kin.keys()
ks.sort()
for k in ks:
  k2 = k.split(" ")
  print >>outfile, "%s\t%s\t%s" % (k2[0], k2[1], kin[k])
outfile.close()

