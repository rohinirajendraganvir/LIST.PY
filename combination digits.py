# def comb(L):
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 if i!=j and j!=k and i!=k:
#                     print(L[i],L[j],L[k])
# comb([2,3,4,])

# a=[3,4,5]
# i=0
# j=0
# k=0
# while i<len(a):
#     while j<len(a):
#         while k<len(a):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i],a[j],a[k])
#                 i=i+1
#                 # print(a[i],a[j],a[k])


# list1 = [[], [], [], [], [], 'text', 'text2', [], 'moreText']
# i=0
# a=[]
# while i<len(list1):
#     if list1!=[]:
#         a.append(list1[i])
#     i+=1
# print(a)



# list1 = [[], [], [], [], [], 'text', 'text2', [], 'moreText']
# list2 = []
# for item in list1:
#     if item!=[]:
#         list2.append(item)
# print(list2)

# a= [5, 6, [], 3, [], [], 9]
# b=[]
# for item in a:
#     if item!=[]:
#         b.append(item)
# print(b)

# # list1= [-1,6,7, 5, -64, -14]
# # pos_count, neg_count = 0, 0
# # num = 0

# # while(num < len(list1)):
      
# #     if list1[num] >= 0:
# #         pos_count += 1
# #     else:
# #         neg_count += 1
# #     num += 1
      
# # print("Positive numbers in the list: ", pos_count)
# print("Negative numbers in the list: ", neg_count)


# a=[-3,9,-4,8,7,-1]
# pos_num=0
# neg_num=0
# i=0
# while i<len(a):
#     if a[i]>=0:
#         pos_num=i+1
#     else:
#         neg_num=i+1
#     i=i+1
# print("pos_num in the list",pos_num)
# print("neg_num in the list",neg_num)