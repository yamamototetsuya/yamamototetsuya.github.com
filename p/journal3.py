# coding:cp932

# �����Ƃ̑ݏo�������W�v����i�u���C�N�����𗘗p���āj
current_month = ''
current_freq = 0
f = open('bjournal.txt')
for line in f:
  d = line[:-1].split(",")
  k = d[0][0:7]
  # �u���C�N���N�������H
  if k != current_month:
    if current_freq > 0:
      print "%s �݂̑��o������: %d" % (current_month,
                                       current_freq)
    # �������Ă��錎�ƃJ�E���^�̃��Z�b�g
    current_month = k
    current_freq = 0
  current_freq += 1

if current_freq > 0:
  print "%s �݂̑��o������: %d" % (current_month,
                                   current_freq)

