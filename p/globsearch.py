# coding:cp932

import glob

# ��������̃L�[���[�h�Ŕ����o���܂�
keyword = '�N���X�V'

# ����̕\�����i����̏ꍇ�����j����֐�
def handle_nippou(d, c):
  if keyword in c:
    print d
    print c

# �t�@�C������C������ЂƂ����ׂ�֐�
def search_file(filename):
  f = open(filename)
  n_date = ''
  n_content = ''
  firstline = 1
  # ����t�@�C������s���ǂݍ���
  for line in f:
    # ���t��ǂݍ���
    if firstline == 1:
      firstline = 0
      n_date = line[:-1]
      continue
    # ���񂪈��؂肵���̂ŁC�\������
    if line.startswith('---'):
      handle_nippou(n_date, n_content)
      # �\���������ƂŁC���ϐ������Z�b�g
      n_date = ''
      n_content = ''
      firstline = 1
      continue
    # ����Ƀf�[�^�t������
    n_content += line
  # �Ō�̓���
  handle_nippou(n_date, n_content)

# ����t�@�C�������ׂĒ��ׂ�
files = glob.glob('nippou_*.txt')
for f in files:
  print "*** ����t�@�C���F%s" % f
  search_file(f)

