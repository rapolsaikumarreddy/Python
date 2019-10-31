
#string Formatting
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
grades = [35, 66, 87, 99, 100]
total = 0
length = len(grades)
for grade in grades:
    total += grade
print(total/length)

#list comprehensions
numbers = [1,2,4,5]
double_num = [x * 2 for x in numbers]
print(double_num)
friends = ["rolf", "sam", "samantha", "saurabh"]
starts_s = [friend for friend in friends if friend.startswith("s")]

for fri in friends:
    if fri.startswith("s"):
        starts_s.append(fri)
    
print(starts_s)

#Dictionaries
friends_ages = {"rapol": 24, "vik": 40, "nag":27}
print(friends_ages["rapol"])
friends_ages["vik"] = 24
print(friends_ages)
friends = [
    {"name": "rapol", "age": 24},
    {"name": "vik", "age": 27},
    {"name": "nag", "age": 26},
]
print(friends[1]["age"])
for friend in friends_ages:
    print(f"{friend}: {friends_ages[friend]}")
# or alternate method for above (for loop)
for friend, age in friends_ages.items():
    print(f"{friend}: {age}")
# caluclating average age of friends_ages
friends_ave = friends_ages.values()
print(sum(friends_ave) / len(friends_ave))

#Destructuring variables
t = 1, 2
x, y = t
print(x, y)
#tuples in list
people = [("bob", 40, "mechanic"), ("james", 79, "artist"), ("harry", 26, "engineer")]
for person in people:
    print(f"Name: {person[0]}, age: {person[1]}, profession: {person[2]}")
# ignoring the variable using _ keyword
people = ("bob", 40, "mechanic")
name, _,profession = people
print(name,profession)
#head and tail in python
head, *tail = [1,2,3,4,5]
print(head)
print(tail)

#functions in python
def hello():
    print("hello world")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"your age in seconds is: {age_seconds}")

user_age_in_seconds()
# memory allocation in functions will be different from global variables
#you can not shadow a variable from an outer scope

#functions arguments and parameters
def add(x, y=8): #parameters and y is optional parameter
    results = x+y
    return x+y # returns value of sum
    print(results)

add(3,5) #positional arguments
add(x=5,y=3) #named or keyword arguments
add(5,y=3) #positional arguments should go first
#function returns null by default 

#lambdas in python
#lambdas are functions without name
(lambda x, y: x+y)(5,7)
def double(x):
    return x * 2
sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
#doubled1 = list(map(lambda x: x * 2 sequence))

#dictionary comprehensions
users = [ 
    (0, "rolf", "password"),
    (1, "bob", "bob123!"),
    (2, "harry", "harry123"),
]
username_mapping = {user[1]: user for user in users}
print(username_mapping)
_, username, password = username_mapping["rolf"]

student = {"name": "jose", "school": "computing", "grades": (66, 77, 88) }
print(student["grades"])

#unpacking arguments
#collecting multiple arguments into single variable
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return (total)
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator provided to apply()"
print(apply(1,2,33, operator="*"))
print(multiply(1,2,3))
def add(x,y):
    return x+y
nums = [3, 5]
print(add(*nums))
nums = {"x":4,"y":3}
print(add(**nums))

#unpacking keyword argumets
def named(**kwargs):
    print(kwargs)
details = {"name": "bob","age": 25}
named(**details)
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
print_nicely(name="bob", age=25)