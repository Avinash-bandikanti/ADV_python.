from collections import defaultdict, Counter,OrderedDict,ChainMap
d=defaultdict()
d['b']=2
d['a']=1
d['c']=3
print(d)
c=defaultdict(list)
c['x']=[1,2,3,4]
print(c)
l=[11,11,11,22,22,33,333,333,3,5,5,2,4,2]
l2=Counter(l)
print(l2)
o=OrderedDict()
o['a']=3
o['b']=2
o['c']=1
print(o)
for k,v in o.items():
    print(k,v)
dict1={'a':123,'b':3432}
dict2={'x':2344,"t":232}
dt=ChainMap(dict1,dict2)
print(dt)
print(dt['a'])