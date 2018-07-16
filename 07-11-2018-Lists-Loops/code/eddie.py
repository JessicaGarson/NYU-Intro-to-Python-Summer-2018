for number in range(99, -1, -1):
    if number > 1:
        print('{} bottles of beer on the wall {} bottles of beer, take one down pass it around {} bottles of beer on the wall.'.format(number, number, number - 1))
    elif number == 1:
        print('{} bottle of beer on the wall {} bottle of beer, take one down pass it around no more bottles of beer on the wall.'.format(number, number))
    else:
        print('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')
