def divide(x,y):
    try:
        print(f'Value of x is : {x}')
        print(f'Value of y is : {y}')
        print(f'{x} divided by {y} is :{x/y}')
    except:
        print('You are trying to divide a number by zero which is invalid')
    finally:
        print('Operation complete!')
if __name__ == "__main__":
    print('Enter the values of x and y below, seperated by spaces : ')
    x, y = [int(x) for x in input().split()]
    divide(x,y)