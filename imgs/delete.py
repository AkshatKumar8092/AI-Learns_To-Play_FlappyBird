a =[2,4,6,8,10,12,14,16,18,20]
n = 3



# b = []
# j = 0
# for i in range(n, len(a)):
#     b.append(a[i])
#     j+=1
#     if i+1 == len(a):
#         for k in range(0,n):
#             b.append(a[k])



# print(b)



# temp = a
# print(temp.pop(0))


k = 0
count = 0
for i in range(0,len(a)):
    if count==n:
        break
    temp = a.pop(k)
    a.append(temp)
    count+=1

print(a)


# ans = [3,4,5,1,2]