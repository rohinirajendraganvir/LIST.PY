# a=['flour','cheese','carrots']
# print("=>"+a[0])
# print("=>"+a[1])
# print("=>"+a[2])

# b=("abc","def","efg")
# print("=>"+b[0])
# print("=>"+b[1])
# print("=>"+b[2])

# x=["horce","ox","buffalow"]
# print("=>"+x[2])
# print("=>"+x[1])
# print("=>"+x[0])

# a=[['i','m'],['h','a','p','p','y'],['i','n','m','y'],['l','i','f','e']]
# b=[]
# c=""
# i=0
# while i<len(a):
#     b.extend(a[i])
#     i=i+1
# print("".join(b))

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
li1=[]
while i<len(list1):
    if list1[i] not in li1:
        li1.append(list1[i])
    i+=1
print(li1)