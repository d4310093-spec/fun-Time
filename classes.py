 class myclass:
     x=5
p1=myclass()
# p2=myclass()
# p3=myclass()
# del p1
# print(p1.x)
# print(p2.x)
# print(p3.x)



# class man:
#     def __init__(person,name,age):
#         person.name=name
#         person.age=age
# p1=man("dheeraj",21)
# print(p1.name)
# print(p1.age)


# class man:
#     def __init__(person,name,age=18):
#         person.name=name
#         person.age=age
#  
# p1=man("dheeraj")
# p2=man("Dk",21)
# print(p1.name,p1.age)
# print(p2.name,p2.age)



# class man:
#     def __init__(detail,name,age,city,state,country,education):
#         detail.name=name
#         detail.age=age
#         detail.city=city
#         detail.state=state
#         detail.country=country
#         detail.education=education 

# p1=man("Dheeraj Kumawat",21,"Ujjain","Madhya Pradesh","India","UG")
# print("Name :-",p1.name)
# print("Age :-",p1.age)
# print("City :-",p1.city)
# print("State :-",p1.state)
# print("Country :-",p1.country)
# print("Education :-",p1.education)



# class Man:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         return "hello, "+self.name
    
#     def Welcome(self):
#         message=self.greet()
#         print(message +"! Welcome to our website")
# d1=Man("Dheeraj")
# d1.Welcome()


# class Car:
#     def __init__(self,brand):
#         self.brand=brand
#     def show(self):
#         print(self.brand)
# c1=Car("Ford")
# c1.show()


# class Person:
#   species = "Human"  # Class property
#   def __init__(self, name):
#     self.name = name  # Instance property
# p1 = Person("Emil")
# p2 = Person("Tobias")
# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1
#     print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()
# p1.celebrate_birthday()
# p1.celebrate_birthday()
# p1.celebrate_birthday()
# p1.celebrate_birthday()


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} ({self.age})"    

# p1 = Person("Tobias", 36)

# print(p1)


# class Playlist:
#   def __init__(self, name):
#     self.name = name
#     self.songs = []

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

#   def remove_song(self, song):
#     if song in self.songs:
#       self.songs.remove(song)
#       print(f"Removed: {song}")

#   def show_songs(self):
#     print(f"Playlist '{self.name}':")
#     for song in self.songs:
#       print(f"- {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to heaven")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.remove_song("Stairway to heaven")
# my_playlist.show_songs()


# class Reactangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
 
# r1=Reactangle(5,3)
# print(r1.area())



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()




# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.year = year
#     self.graduationyear = 2026

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# print(x.year)
# print(x.graduationyear)
# x.welcome()




# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()





# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()



# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)
