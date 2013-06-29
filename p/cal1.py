import calendar
calendar.setfirstweekday(6)

y = 2012
m = 4

c = calendar.monthcalendar(y, m)
for w in c:
  print "<tr>"
  for d in w:
    if d != 0:
      print "<td>%s</td>" % d
    else:
      print "<td></td>"
  print "</tr>"

