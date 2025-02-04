# data = [int(i) for i in input().split()]
# n = data[0]
# m = data[1]
# h = [int(i) for i in input().split()]
#
# k =[]
# # for i in range(len(h)-1):
# #     k.append(abs(h[i]-h[i+1]))
# # maxh=maxh
# # if k.count(maxh)==m-1:
# #     for i in range(k.count(maxh)):
# #         k.append(maxh)
# #     maxh = maxh
# #     print(maxh)
# # else:
# #     print(-1)
#
# for i in range(len(h)-1):
#     k.append(abs(h[i]-h[i+1]))
# maxh=max(k)
# maxh = maxh
#
# d = [i for i in range(n)]
# print(h)
# print(d)
# print(k)
# print(maxh)
# for i in range(k.count(maxh)):
#     k.remove(maxh)
# print(k.count(maxh))
#
#
# for i in d:
#     if k.count(maxh) == m-1:
#         print(f"zxcc {maxh}")
#         break
#
#     elif k.count(maxh) !=m-1:
#         k.remove(maxh)
#         print(f'qwe {k}')
#     elif i == d[-1]:
#         print(-1)
#         break
from typing import reveal_type

data = [int(i) for i in input().split()]
n = data[0]
m = data[1]
h = [int(i) for i in input().split()]
k = [i for i in range(n)]

for i in range(len(h)-1):
    k[i] = abs(h[i]-h[i+1])

b=k
maxh = max(k)

for i in range(k.count(maxh)):
    k.remove(maxh)

maxh = max(k)
def func(b, k, maxh):
    if k.count(maxh)==m-1 and maxh!=b[-1] and maxh!=b[0]:
        return print(maxh)
    else:
        k.remove(maxh)
        func(k, maxh)


func(b, k, maxh)