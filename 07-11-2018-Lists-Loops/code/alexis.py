for number in range(99, 0, -1):
    if number > 1:
        print('{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer on the wall.'.format(number,number,(number-1)))
    else:
        print("If that one bottle should happen to fall, what a waste of alcohol!")
