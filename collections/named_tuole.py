from collections import namedtuple
Person=namedtuple('person',['name','age','gender'])
p=Person("asd",234,'asdfdss')
print(p.name)
print(p.age)
print(p.gender)