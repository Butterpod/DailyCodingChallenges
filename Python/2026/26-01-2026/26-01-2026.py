def fizz_buzz_mini(n):
    if (n%3==0 and n%5==0):
        return "FizzBuzz"
    elif (n%5==0):
        return "Buzz"
    elif (n%3==0):
        return "Fizz"
    else:
        return str(n)

fizz_buzz_mini(3) # "Fizz".
fizz_buzz_mini(4) # "4".
fizz_buzz_mini(35) # "Buzz"
fizz_buzz_mini(75) # "FizzBuzz".
fizz_buzz_mini(98) # "98".