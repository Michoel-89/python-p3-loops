#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while(num > 0):
        print(num)
        num -= 1
    print('Happy New Year!')

def square_integers(int_list):
    ints_squared = list()
    for int in int_list:
        ints_squared.append(int ** 2)
    return ints_squared

def fizzbuzz():
   for i in range(1, 101):
       
       if(i % 3 == 0 and i % 5 == 0):
           print("FizzBuzz")
       elif(i % 3 == 0 and i % 5 != 0):
           print("Fizz")
       elif(i % 3 != 0 and i % 5 == 0):
           print("Buzz")
       else:
           print(i)
