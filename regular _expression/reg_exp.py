import re
#pattern=r"\d+"
pattern=r"(hcl)"
str1="hello from hcl bangolorehcl 5456 5466788 hcl"
#m=re.findall(pattern,str1)
m=re.search(pattern,str1)
print(m)