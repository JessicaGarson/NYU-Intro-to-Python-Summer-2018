name = input('Enter your name: ')
print('The name you entered is {}'.format(name))


# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


# Define main method that calls other functions
def main():
    has_vowel()

main()

#
# # Execute main() function
# if __name__ == '__main__':
#     has_vowel() # Code to run when this is the main program here.
