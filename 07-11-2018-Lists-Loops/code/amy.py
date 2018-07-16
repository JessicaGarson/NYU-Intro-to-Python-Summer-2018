for bottles in range(99,-1,-1):
    if bottles >=2:
        print(str(bottles) + 'bottles of beer on the wall,'+ str(bottles) + 'bottles of beer.')
        print('Take one down and pass it around,'+ str(bottles-1) +' bottles of beer on the wall.')
    elif bottles ==1:
        print('1 bottle of beer on the wall, 1 bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    else:
        print('No more bottles of beer on the wall, no more bottles of beer. ')
        print('Go to the store and buy some more, 99 bottles of beer on the wall.')
