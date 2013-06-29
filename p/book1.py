# coding:utf-8

# 新着図書リスト（完成！）

# 教員推薦図書リストを読み込んでおく
recommend = []
for line in open('recommend.txt'):
  recommend.append(line[:-1])

print """
<html>
<head>
<meta http-equiv="Content-Type"
      content="text/html; charset=utf-8" />
<link rel="stylesheet" href="fancytable.css" />
<title>新着図書リスト</title>
</head>
<body>
<h1>新着図書リスト</h1>
<p>ピンク色は，教員推薦図書です。</p>
<table border="1">
<tr>
<th>図書ID</th><th>書名</th><th>記号</th>
</tr>
"""
current_date = ''
f = open("newbooks.txt")
for line in f:
  a = line[:-1].split("\t")
  if current_date != a[2]:
    print "<tr>"
    print '<th colspan="4">%s 配架分</th>' % a[2]
    print "</tr>"
    current_date = a[2]
  if a[0] in recommend:
    print '<tr class="recommend">'
  else:
    print "<tr>"
  print "<td>%s</td><td>%s</td><td>%s</td>" % (a[0],
            a[1], a[3])
  print "</tr>"

print """
</table>
</body>
</html>
"""

