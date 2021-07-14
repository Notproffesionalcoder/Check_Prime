# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 2:
    # check for factors
    for i in range(2, int(pow(num, .5))+1):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
elif num == 2:
    flag = True
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
