l= [-1,6,7, 5, -64, -14,8]
num = 0
pos_count=0
neg_count=0
while num < len(l):
    if l[num]>= 0:
        pos_count += 1
    else:
        neg_count +=1
    num=num+1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)


# l= [-1,6,7, 5, -64, -14]
# i=0
# a=[]
# b=[]
# while i<len(l):
#     if l[i]>0:
#         a.append(l[i]) 
#     else:
#         b.append(l[i])
#     i=i+1
# print(a)
# print(b)

# list1 = [-10, 21, -4, -45, -66, 93]
# num = 0

# while(num < len(list1)):
#     if list1[num] >= 0:
#         print(list1[num], end = " ") 
    

#     num += 1