# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(names_list)
# names_list.append("dhruv")
# print("length of the list is ", len(names_list))
# print(names_list)


# names_list=["mango","orange","apple"]
# # print(names_list)
# names_list.append("jacfruit")
# print(len(names_list))
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.append("alok")
# print("length of the list is ", len(names_list))
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# names_list.pop()
# print("length of the list is ", len(names_list))
# print(names_list)

# names_list=["mbpc","jmpc","jnv","ng"]
# names_list.pop()
# print(names_list)
# print(len(names_list))


# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("length of the list is ", len(names_list),names_list)
# names_list.pop(2)
# print("length of the list is ", len(names_list),names_list )
# names_list.pop(2)
# print("length of the list is ", len(names_list),names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("shivam" in names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# if "shivam" in names_list:
#       print("Shivam ka naam names_list mei hai")
# else:
#     print("Shivam ka naam names_list mei nahi hai.")

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

a=["12","23","34"]
i=0
b=[]
sum=0
while i<len(a):
    sum=sum+a[i]
    b.append(sum)
    i=i+2
print(sum)