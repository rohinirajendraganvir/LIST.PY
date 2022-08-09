# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# for num in range(start, end + 1):
    
#     if num < 0:
#         print(num, end = " ")



# word = "https://www.w3resource.com/python-exercises/list/"
# lst = ['/', '.edu', '.tv']


# if any(ext in word for ext in lst):
#     print(True)
# else:
#     print(False)

# a=[[1, 2, 4], [2, 4, 4], [1, 2]]
# print(a[0][0])
# i=0
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a):
#         if i<=j:
#           s+=a[i][j]
#         j=j+1
#     i+=1
# print(b)

a=[1, 2, 3, 4, 5, 6]
i=0
list=[]
while i<len(a)-1:
    b=[a[i],a[i+1]]
    list.append(b)
    i=i+1
print(list)


    