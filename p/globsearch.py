# coding:cp932

import glob

# 日報をこのキーワードで抜き出します
keyword = '年次更新'

# 日報の表示を（特定の場合だけ）する関数
def handle_nippou(d, c):
  if keyword in c:
    print d
    print c

# ファイルから，日報をひとつずつ調べる関数
def search_file(filename):
  f = open(filename)
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

# 日報ファイルをすべて調べる
files = glob.glob('nippou_*.txt')
for f in files:
  print "*** 日報ファイル：%s" % f
  search_file(f)

