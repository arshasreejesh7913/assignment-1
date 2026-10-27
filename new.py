# s="3"
# s2=3
# print(s*s2)
# a= input("enter the name")
# print(a)
# name=input("enter your name")
# print("hello",name)

# num=int(input("enter the number"))
# if num%2==0:
#     print(num)
# else:
#     print("odd number")

# num=int(input("enter the number"))
# if num>0:
#     print("number is positive")
# else:
#     print("number is negative")


# multiplication table 

# num=int(input("enter the number"))
# i=1
# while i<=10:
#      print(num, "x", i, "=", num * i)
#      i=i+1
row=1
while row<=3:
    col=1
    while col<=3:
        print("*  ",end="")
        col+=1
    print()
    row+=1