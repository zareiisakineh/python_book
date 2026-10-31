# file: ex_06_03_proper_divisors_start.py

# TODO: Write a function proper_divisors(n: int) -> list
def proper_divisors(n: int) -> list:
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return divisor
#       Returns a list of all proper divisors of n
#       (positive integers less than n that divide n evenly)
#       Hint: use range(1, n) and check n % i == 0

# TODO: Write a function is_perfect(n: int) -> bool
def is_perfect(n: int) -> bool:
    summen = sum(proper_divisors(n))
    if summen == n:
        return True
    else:
        return False
    
#       Returns True if n is a perfect number
#       (sum of proper divisors equals n)
#       Hint: use sum() on the result of proper_divisors()

if __name__ == "__main__":
    # TODO: Read a number from the user and display its proper divisors
    #       Example: "Proper divisors of 12: [1, 2, 3, 4, 6]"
    tall = int(input("Skriv et tall for å regne ut proper devisor: "))
    print(f"Proper devisors av tallet: {tall} er:  {proper_divisors(tall)}")
    
 
    # TODO: Find and display all perfect numbers up to 10000
    #       Example: "Perfect numbers up to 10000: [6, 28, 496, 8128]"
    perfekt_list = []
    for nummer in range(1, 10001):
        if is_perfect(nummer):
            perfekt_list.append(nummer)
    print(f"Perfect numbers up to 10000: {perfekt_list}")
