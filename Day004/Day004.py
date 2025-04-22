#randomisation and python lists
import random
import my_module

print(my_module.my_favourite_number)

random_integer= random.randint(1,55)
print(random_integer)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float= random.uniform(1,10)
print(random_float)

random_number_ht= random.randint(1,4)
print(random_number_ht)
if random_number_ht == 1 or random_number_ht== 3 :
    print("Head")

else:
    print("Tail")