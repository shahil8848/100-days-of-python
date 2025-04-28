# function parameter and ceaser cipher
#functions with inputs
#positional vs keyword arguments
def greet():
    print("Hello ")
    print("How are you ")
    print("Shine bright like a diamond")

greet()

#function that allows for inputs

def greet_with_name(name):
    print(f"hello {name}")
    print(f"How do you do {name}")

greet_with_name("Shahil")
greet_with_name("Angela")
#parameter and argument



def life_in_weeks(age):
    remaining_age = 90 -age
    weeks=remaining_age* 52
    print(f"You have {weeks} weeks left")

life_in_weeks(int(input("Enter your age:")))