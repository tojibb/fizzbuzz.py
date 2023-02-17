#fizzbuzz.py

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")

#if the value of fizzbuzz is divided by 3 and the remainder is 0 also if fizzbuss is divided by 5 and the remainder is 0 print the word fizzbuzz  

    elif fizzbuzz % 3 == 0:
        print("fizz")

#if the value of fizzbuzz is divided by 3 and the remainder is 0 print the word fizz  

    elif fizzbuzz % 5 == 0:
        print("buzz")

#if the value of fizzbuzz is divided by 5 and the remainder is 0 print the word buzz  

    else:
        print(fizzbuzz)

#else print the value of fizzbuzz if fizzbuzz is divided by 3 and the remainder is not 0 also if fizzbuss is divided by 5 and the remainder is not 0
