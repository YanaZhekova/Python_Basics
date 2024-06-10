command = input()
sum_primes = 0
sum_non_primes = 0
counter = 0
while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter > 2:
            sum_non_primes += number
            counter = 0
        else:   
            sum_primes += number
            counter = 0
        command = input()

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
