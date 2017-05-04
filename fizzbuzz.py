import sys

if len(sys.argv) == 1:

    try:
        n = input("Til what number are we Fizz Buzzing to? ")
        print("Fizz Buzz counting up to {}".format(n))

    except NameError:
        print("Please enter a number!")
        n = input("Til what number are we Fizz Buzzing to? ")
        print("Fizz Buzz counting up to {}".format(n))

    for n in range(1,n):
        if n % 3 == 0 and n % 5 == 0:
            print "FizzBuzz"
        elif n % 3 == 0:
            print "Fizz"
        elif n % 5 == 0:
            print "Buzz"
        else:
            print n


elif len(sys.argv) == 2:

    try:
        n = int(sys.argv[1])
        print("Fizz Buzz counting up to {}".format(n))

    except ValueError:
        print("Please enter a number!")
        n = input("Til what number are we Fizz Buzzing to? ")
        print("Fizz Buzz counting up to {}".format(n))

    for n in range(1,n):
        if n % 3 == 0 and n % 5 == 0:
            print "FizzBuzz"
        elif n % 3 == 0:
            print "Fizz"
        elif n % 5 == 0:
            print "Buzz"
        else:
            print n


else:

    print("The number of arguments provided is invalid. We're Fizz Buzzing til 100 yo.")
    n = 100
    print("Fizz Buzz counting up to {}".format(n))

    for n in range(1,n):
        if n % 3 == 0 and n % 5 == 0:
            print "FizzBuzz"
        elif n % 3 == 0:
            print "Fizz"
        elif n % 5 == 0:
            print "Buzz"
        else:
            print n
