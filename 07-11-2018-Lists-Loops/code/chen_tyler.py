
for number in range(99, 0, -1):

    if number >=3 :
        print("{} bottles of beer on the wall".format(number))
        print("{} bottles of beer".format(number))
        print("Take one down, pass it around")
        print("{} bottles of beer on the wall".format(number-1))

    elif number==2 :
        print("{} bottles of beer on the wall".format(number))
        print("{} bottles of beer".format(number))
        print("Take one down, pass it around")
        print("{} bottle of beer on the wall".format(number-1))

    else:
        print("{} bottle of beer on the wall".format(number))
        print("{} bottle of beer".format(number))
        print("Take one down, pass it around")
        print("{} bottles of beer on the wall".format(number-1))
