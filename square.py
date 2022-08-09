# number=str(input("Enter the number :"))
# def pc(number):
#   digits = list(number)
#   for j in digits:
#         print(int(j)**2,end="")
# pc(number)

num=int(input("enter the number.."))
mul = 1    
while (num > 0):
     dig = num % 10    
     if (dig > 0):   
         mul= (dig * mul)    
     num = num / 10 
     mul = mul * 10    

# from itertools import groupby
# def encode_list(s_list):
#     return [[len(list(group)), key] for key, group in groupby(s_list)]
# n_list = [1,1,2,3,4,4.3,5, 1]
# print("Original list:") 
# print(n_list)
# print("\nList reflecting the run-length encoding from the said list:")
# print(encode_list(n_list))
# n_list = 'automatically'
# print("\nOriginal String:") 
# print(n_list)
# print("\nList reflecting the run-length encoding from the said string:")
# print(encode_list(n_list))