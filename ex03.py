#32
a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
c=a|b
d=a&b

print(c)
print(d)

#33
a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
c=a-b
d=a^b

print(c)
print(d)

#34
a={1,2,3,4}
a|={5}
print(a)

#35
a={100,200,300,400}
a&={400,500,600,700,800}
print(a)

b={100,200,300,400}
b-={400,500,600,700,800}
print(b)

c={100,200,300,400}
c^={400,500,600,700,800}
print(c)

#36
a={100,200,300,400,500}
b={100,200,300,400,500}

if a.issuperset(b) and a.issubset(b):
    print('동시')
elif a.issuperset(b):
    print('상위')
elif a.issuperset(b):
    print('부분')

#37
a={2,8,13,21}
a.add(1000)
removed_value=a.pop()
print(a)

#38
multiples={x for x in range(1,101) if x%3 ==0 and x%5==0}
print(multiples)