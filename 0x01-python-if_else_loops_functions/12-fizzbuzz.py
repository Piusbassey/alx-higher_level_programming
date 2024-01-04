def fizzbuzz():


    for i in

    range(1, 101):
        if i % 3 == 0

        and i % 5 == 0:
            print("Fizzbuzz", end=" ")
        elif i % 3:
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
            print()

            fizzbuzz()

