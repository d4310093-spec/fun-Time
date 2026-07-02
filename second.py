# marks=int(input ("enter your marks :-"))
# if (marks>=80):
#     print("a grade")
# elif (marks>=60):
#     print("b grade")
# elif    (marks>=40):
#     print ("c grade")    
# elif (marks>=30):
#     print ("d grade")
# else:
#     print ("fail")




# a=int(input("enter a number :-"))
# if (a%2==0):
#     print(a,"is even number")
# elif(a%2!=0):
#     print(a,"is odd number")
# else:
#     print(a,"is zero")


# age=int(input("enter your age :-"))
# if (age>=18):
#     print ("you are eligible to vote ")
# else :
#     print ("you can not vote")\


# name =str (input ("enter your name :-"))
# age=str (input ("enter your age :-"))
# mobile =str (input ("enter you mobile number :-"))             
# print ("------------------------------")
# print (name)
# print (age)
# print (mobile)


# x=int(input("enter a nnumber :-"))
# match x:
#     case 1:
#         print("monday")
#     case 2:
#         print ("tuesday")
#     case 3:
#         print ("wednesday")
#     case 4:
#         print ("thursday")
#     case 5:
#         print ("friday")
#     case 6 :
#         print ("saturday") 
#     case 7:
#         print ("sunday")
#     case _:
#         print("invalid number")


# x=int (input ("inter a number :-"))
# match x:
#     case 1:
#       print ("january")
#     case 2:
#       print ("february")
#     case 3:
#       print ("march")
#     case 4:
#       print ("april")
#     case 5:
#         print ("may")
#     case 6:
#         print ("june")
#     case 7:
#         print ("july")
#     case 8:
#         print ("august")
#     case 9:
#         print ("september")
#     case 10:
#         print ("october")
#     case 11:
#         print ("november")
#     case 12:
#         print ("december")
#     case _:
#       print ("error")



a=int (input("enter a number ="))
syn=str (input ("enter a symbol ="))
b=int (input ("enter a number ="))
match syn:
    case '+':
        print (a+b)
    case '-':
        print (a-b)
    case '*':
        print (a*b)
    case '/':
        print (a/b)
    case _:
        print ("error")            