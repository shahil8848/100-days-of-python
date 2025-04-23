# student_score=[150,59,325,494,43,3,43,439,39,429,659,29,219,9,439,92,439,239,239,2,329]
#
# print(max(student_score))
#
# total_score= sum(student_score)
# print(total_score)
#
# sum=0
# for score in student_score:
#     sum +=score
#
# print(sum)
#
# max_number=0
# for score in student_score:
#     if max_number< score:
#         max_number=score
#
# print(max_number)

for number in range(1,101):
    if number%3 ==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)