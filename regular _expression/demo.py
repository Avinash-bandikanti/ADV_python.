import re
l="10.20.30.34 200.34"
a=r'.'
m=re.findall(a,l)
print(m)