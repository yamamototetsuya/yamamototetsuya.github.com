# coding:cp932

# 日報をこのキーワードで抜き出します
keyword = '年次更新'

# 日報の表示をする関数
def handle_nippou(d, c):
  if keyword in c:
    print "*** 日報 ***"
    print d
    print c

f = open('nippou.txt')
n_date = ''
n_content = ''
firstline = 1
# 日報ファイルを一行ずつ読み込む
for line in f:
  # 日付を読み込む
  if firstline == 1:
    firstline = 0
    n_date = line[:-1]
    continue
  # 日報が一区切りしたので，表示する
  if line.startswith('---'):
    handle_nippou(n_date, n_content)
    # 表示したあとで，諸変数をリセット
    n_date = ''
    n_content = ''
    firstline = 1
    continue
  # 日報にデータ付け足し
  n_content += line
# 最後の日報
handle_nippou(n_date, n_content)

