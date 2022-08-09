a=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
b=[]
c=""
while i<len(a):
    
    b.extend(a[i])
    i=i+1
print(["".join(b)])


# a=[['r','o','h','i','n','i'],['g','a','n','v','r'],['s','d','k'],['s','j','h']]
# b=""
# c=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b+=(a[i][j])
#         j+=1
#     i+=1
# c.append(b)
# print(c)

# a=[['j','w','h','a','r'],['n','v','o','d','a','y'],['v','i','d','y','a','l','a','y']]
# b=[]
# c=""
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c+=(a[i][j])
#         j+=1
#     i+=1
# b.append(c)
# print(b)
# ....or
# while i<len(a):
#     b.extend(a[i])
#     i=i+1
# print("".join(b))

# a=[['i','m'],['h','a','p','p','y'],['i','n','m','y'],['l','i','f','e']]
# b=""
# c=[]
# i=0
# while i<len(a):
#     c.extend(a[i])
#     i=i+1

# print("".join(c))

# a=int(input("enter the time"))
# if a>="7:00" and a<="7:59":
#     print("fresh up")
# elif a>="8:00" and a<="8:59":
#     print("good")
# else:
#     print("noyhing")
