from random import randint

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ['_','&','^','$','*']

def generate_password(length_of_password, include_alphabets, include_numbers, include_special_chars):
    chars = []
    password = ''
    if include_alphabets:
        chars += alphabets
    if include_numbers:
        chars += numbers
    if include_special_chars:
        chars += special_chars
    for _ in range(length_of_password):
        password += chars[randint(0, len(chars)-1)]
    return password

if __name__ == '__main__':

    include_alphabets = False
    includes_numbers = False
    includes_special_chars = False

    print('Welcome to password generator')
    print()
    print('  *****  ')
    print(' *** *** ')
    print('***   ***')
    print('*********')
    print('*********')
    print('***   ***')
    print('**** ****')
    print('**** ****')
    print('*********')
    print()

    print('To generate a password first let us know')
    print('=========================================')
    print('Should password contain alphabets?')
    include_alphabets = input('(y/n): ') == 'y'
    print('Should password contain numbers?')
    includes_numbers = input('(y/n): ') == 'y'
    print('Should password contain special characters?')
    includes_special_chars = input('(y/n): ') == 'y'
    print('=========================================')
    print()

    print(generate_password(8, include_alphabets, includes_numbers, includes_special_chars))