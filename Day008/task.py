#functions with more than 1 input
#positional vs keyword arguments

def greet_with(name,location):
    print(f"Hello my name is {name}")
    print(f"I am from {location}")

greet_with("Shahil","Nepal")
  #why this

#keyword arguments
greet_with(location="Nepal",name="Shahil Bhusal")

