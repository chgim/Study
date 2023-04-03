a=[20,10,30]
print(a)
a.extend(a)
print(a)
a.pop()
print(a)
a.reverse()
print(a)

b=[3,5,7,8]
b.append(4)
print(b)
b.insert(2,8)
print(b)
b.remove(8) # 가장 앞에 있는 값 부터 삭제
print(b)