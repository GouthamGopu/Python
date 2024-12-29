from functools import reduce

sq=lambda x:x*x

print(sq(10))

l=['goutham','dimpu']

name="_".join(l)

print(name)

# format functions are used before f strings version now we mostly dont use
str="{} is a good {}".format("goutham", "boy") 
print(str)


n=[1,2,3,4,5]

m=list(map(sq,n))
print(m)


mul2 = lambda x: True if int(x) % 2 == 0 else False

f = list(filter(mul2, n))

print(f)


sum=lambda a,b:a+b

r=reduce(sum,n)
print(r)