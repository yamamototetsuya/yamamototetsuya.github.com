# coding:cp932

# ��������̃L�[���[�h�Ŕ����o���܂�
keyword = '�N���X�V'

# ����̕\��������֐�
def handle_nippou(d, c):
  if keyword in c:
    print "*** ���� ***"
    print d
    print c

f = open('nippou.txt')
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

