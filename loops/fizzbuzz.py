# 1
# 2
# Fizz
# 4
# Buzz


def fizz_buzz(start, max_value):
  num_list = range(start, max_value)
  for num in num_list :
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif 0 == num % 5:
      print('Buzz')  
    elif 0 == num % 3:
      print('Fizz')
    else:
      print(num)

fizz_buzz(1,50)