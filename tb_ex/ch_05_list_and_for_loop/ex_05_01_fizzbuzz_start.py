# file: ex_05_01_fizzbuzz_start.py

# TODO: Loop through integers 1 to 100 using range()
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
         print("Buzz")
    else:
        print(i)
    # TODO: If divisible by both 3 and 5: print "FizzBuzz"
    #       If divisible by 3 only: print "Fizz"
    #       If divisible by 5 only: print "Buzz"
    #       Otherwise: print the number
    #
    #       Hint: check the combined condition (divisible by both) first
