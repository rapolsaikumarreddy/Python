#string Formatting
'''
name = "rapol"
print(f"my name is {name}")
greeting = "hello {}"
with_format = greeting.format("rapol")
print(with_format)
longer_phrase = "hello {}, today is {}"
with_format1 = longer_phrase.format("rapol", "monday")
print(with_format1)
#getting user input
user_name = input("what is your name: ")
print(f"hello {user_name}")
#converting string input to integer 
size_input = input("how big is your house(in square feet): ")
square_feet = int(size_input)
square_meter = square_feet / 10.8
print(f"{square_meter:.2f}")
#age app
user_age = int(input("Enter your age: "))
month = int(user_age) * 12
print(f"your age, {user_age} is equal to {month} months")
#lists , tuples and sets
l = ["x", "y", "z"] #you can add or remove elements from list
t = ("x", "y", "z") #you can not add or remove elements from tuple
my_tuple = 15, #single value tuple
s = {"x", "y", "z"} #you can not have duplicates in set
print(l[2]) # subscript notation 
l[0] = "a"
print(l)
l.append("x")
s.add("x")
print(s)
# advance sets operations
friends = {"x", "y", "z"}
abroad = {"x", "s"}
local = friends.difference(abroad)
print(local)
local1 = friends.union(abroad)
print(local1)
both = abroad.intersection(friends)
print(both)
#intro to conditional statements
day_of_week = input("what day of the week is it today: ").lower
if day_of_week == "monday":
    print("Hello world")
elif day_of_week == "tue": 
    print("this is elif")
else:
    print("nothing")
#in keyword 
movies_watches = {"the matrix", "green book", "her"}
user_movie = input("enter something you have watched recently: ")
print(user_movie in movies_watches)
number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()
if user_input == "y":
    guess_number = int(input("Enter a guess number: "))
    if guess_number == number:
        print("you won!")
    elif number - guess_number in (1, -1): 
    # and also you can use absolute function abs(number - user_number) == 1:
        print("you are close but lost")
    else:
        print("you lost")
else:
    print("Thank you")
#while loop in python
number = 7
while True:
    user_input = input("would you like to play? (y/n) ")
    if user_input == "n":
        break
    guess_number = int(input("Enter a guess number: "))
    if guess_number == number:
        print("you won!")
    elif number - guess_number in (1, -1): 
    # and also you can use absolute function abs(number - user_number) == 1:
        print("you are close but lost")
    else:
        print("you lost")
#for loop in python
friends = ["x","y","z"]
for friend in friends:
    print(f"{friend} is my friend")
'''
grades = [35, 66, 87, 99, 100]
total = 0
length = len(grades)
for grade in grades:
    total += grade
print(total/length)
    