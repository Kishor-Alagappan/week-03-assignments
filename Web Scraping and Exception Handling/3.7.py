class InvalidUsernameLength(Exception):
    pass

def check_length(name):
    try:
        if len(name) < 5 or len(name) > 15:
            raise InvalidUsernameLength
    except InvalidUsernameLength: 
        print('Invalid username length!')

if __name__ == '__main__':
    print('Enter the username below to check if it\'s valid or not (valid only if its length is between 5-15 characters)')
    name = input()
    check_length(name)