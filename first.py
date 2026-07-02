          #1st area or perimetre

# l=5
# b=8
# area=l*b
# perimeter=2*(l+b)
# print("length = ",l)
# print("Breadth = ",b)
# print("\n")
# print("Area of rectangle",area)
# print("Perimeter of rectangle",perimeter)

         #2nd meter to feet

# meter=int(input("Enter meter to convert in feet :- "))
# feet=meter*3.2
# print(meter," meter is = ",feet," feet") 

       #   3rd sign up page

# print("Welcome to our website")
# username=str(input('enter your username = '))
# mob=int(input('enter your mobile number = '))
# age=int(input('enter your age = '))
# print('\n')
# print("Username = ",username)
# print("Mobile number = ",mob)
# print("Age = ",age)
# print("Your are registered succesfully")

            #4th gradig system 

# marks=int(input('enter yout marks = '))
# print('marks = ',marks)
# if (marks>=80):
#     print('A Grade')
# elif (marks>=60):
#     print('B Grade')
# elif (marks>=40):
#     print('C Grade')
# elif (marks>=30):
#     print('D Grade')
# else :
#     print('Fail')

#                 # 5th voting system 

# age=int(input("Enter your age = "))
# if (age>=18):
#     print("You can vote")
# elif (age>=13):
#     print("You are teenager")
# else :
#     print("You can not vote")

#        6 th  print months by match case

# month=int(input("Enter Month name in number :- "))
# match month:
#     case 1:
#         print("January")
#     case 2:
#         print("february")
#     case 3:
#         print("March")
#     case 4:
#         print("April")
#     case 5:
#         print("May")
#     case 6:
#         print("June")
#     case 7:
#         print("July")
#     case 8:
#         print("August")
#     case 9:
#         print("September")
#     case 10:
#         print("October")
#     case 11:
#         print("November")
#     case 12:
#         print("December")  
#     case _:
#         print("error")
       
       # 7th print days  by match case

# Day=int(input("Enter Day name in number :- "))
# match Day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")  
#     case _:
#         print("error")

       #      8th calculator by match case

# num1=int(input("Enter First Number :- "))
# sym=str(input("Enter symbol :- "))
# num2=int(input("Enter First Number :- "))
# match sym:
#     case '+':
#         print(num1+num2)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         print(num1/num2)  
#     case _:
#         print("error")    

       #   9th even odd print match case
# num=int(input("Enter a number :- "))
# match (num%2):
#     case 0:
#         print(num,"is Even")
#     case 1:
#         print(num,"is odd")
#     case _:
#         print("Error")

       # 10th posi nega zero by match case

# num=int(input("Enter a number :- "))
# match ((num>0) - (num<0)):
#     case 1:
#         print(num,"is Positive Number")
#     case -1:
#         print(num,"is Negative Number")
#     case 0:
#         print(num,"is Zero")

       #  11th 1 to 10 print

# num=1
# while(num<=10):
#     print(num)
#     num+=1

       #    12th 10 to 1 print

# num=10
# while(num>=1):
#     print(num)
#     num-=1

       #  13th even odd print by while

# num=0
# while(num<=9):
#     num+=1
#     if(num%2==0):
#         print("Even ",num)
#     else:
#         print("Odd",num)

       # 14th even odd sum print by while

# num = 1
# sum = 0
# while num <= 10:
#     if num % 2 == 0:
#         print("Even", num)
#         sum = sum + num
#     num += 1
# print("Sum =", sum)

        # 15th  count the number by while

# a=int(input("Enter some numbers = "))
# count=0
# while a >0:
#     a=a//10
#     count +=1
# print("Number of digits = ",count)

        # 16th table by while

# a=int(input("Enter a number = "))
# b=1
# while b<=10:
#     print(a,"x",b,"=",a*b)
#     b+=1

        # 17th 1 to 10 print

# for i in range (1 , 11):
#     print(i)

        # 18th 10 to 1 print

# for i in range (10,0,-1):
#     print(i)

        # 19th  even odd number print by for

# for i in range (20,197):
#     if i%2==0:
#         print(i,"is even ")
#     else :
#         print(i,"is odd")

        # 20 even number sum by for

# sum=0
# for i in range (1, 11):
#     if i%2==0:
#         print ("even ",i)
#         sum=sum+i
# print("sum = ",sum)

        #  21 table print by for

# a=int(input("Enter a number = "))
# for b in range (1,11):
#     print(a,"x",b,"=",a*b)
  
        # 22 number count by for

# a = input("Enter some numbers = ")
# count = 0
# for digit in a:
#     if digit.isdigit():
#         count += 1
# print("Number of digits =", count)

        # 23 list print 1 number 

# a=[15,24,36,25,25,3]
# print(a[0])

        # 24 even odd print by for in list

# a=[15,24,36,25,25,3]
# for i in range (6):
#     if a[i]%2==0:
#         print("Even ",a[i])
#     else:
#         print("Odd",a[i])

        # 25 negative positive print by for in list

# a=[15,24,-36,25,-25,0,-2,55]
# for i in range (8):
#     if a[i]>0:
#         print("Positive ",a[i])
#     elif a[i]<0:
#         print("Negative ",a[i])
#     else :
#         print("Zero ",a[i])

        # 26  sum of list num by for

# a=[15,24,36,25,25,3]
# sum=0
# for i in range (6):
#     print(a[i])
#     sum=sum+a[i]
# print("Sum = ",sum)

        # 27 number find in list by for

# a=[15,24,36,25,25,3]
# found=int(input("Enter a number to find in list = "))
# for i in range (6):
#     if found==a[i]:
#         print(found,"Found","at index ",i) 
#     else:
#         print("Not Found")
    
        # 28 largest smallest number find in list by for

# a=[15,24,36,25,25,3]
# largest=a[0]
# smallest=a[0]
# for i in range (6):
#     print(a[i])
#     if a[i]>largest:
#         largest=a[i]
#     if a[i]<smallest:
#         smallest=a[i]
# print("Largest number in list = ",largest)
# print("Smallest number in list = ",smallest)

        # 29 number greather than 18 list by for loop
# a=[15,24,36,25,25,3]
# print(a)
# print("Number greather than 18 are :-")
# for i in range (6):
#     if a[i]>18:
#         print(a[i])

         # 30 name find in list by for  
# a=["dheeraj","sujal","mahir"]
# name=str(input("Enter a name to find in list = "))
# for i in range (3):
#     if name == a[i]:
#         print(name,"found at index",i)
#     else :
#         print(name,"not found in list")

         # 31 smallest largest sum and average find in list by for
# a=[15,24,36,25,25,3]
# largest=a[0]
# sum=0
# average=0
# smallest=a[0]
# for i in range (6):
#     print(a[i])
#     if a[i]>largest:
#         largest=a[i]
#     if a[i]<smallest:
#         smallest=a[i]
#     sum=sum+a[i]
#     average=sum/6
# print("Largest number in list = ",largest)
# print("Smallest number in list = ",smallest)
# print("Sum = ",sum)
# print("Average = ",average)

         # 32 table print by function 
# def table ():
#     a=int(input("Enter a number = "))
#     for b in range (1,11):
#         print(a,"x",b,"=",a*b)
# table()

         # 33 calculator by function
# def cal ():
#     num1=int(input("Enter First Number :- "))
#     sym=str(input("Enter symbol :- "))
#     num2=int(input("Enter First Number :- "))
#     match sym:
#         case '+':
#             print(num1+num2)
#         case '-':
#             print(num1-num2)
#         case '*':
#             print(num1*num2)
#         case '/':
#             print(num1/num2)  
#         case _:
#             print("error")    
# cal()

         # 34 digits count by function in while loop 
# def count():
#     a=int(input("Enter some numbers = "))
#     count=0
#     while a >0:
#         a=a//10
#         count +=1
#     print("Number of digits = ",count)
# count()

         # 35
while True:
    first_input = input("Enter first input: ")
    second_input = input("Enter second input: ")

    if first_input == second_input:
        print("Inputs are the same. Restarting...\n")
        continue  # Jumps back to the top of the 'while' loop
    
    print("Inputs are different. Ending program.")
    break  # Exits the loop
