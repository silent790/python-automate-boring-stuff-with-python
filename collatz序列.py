def collatz(x):
    if x % 2 == 0:
        print(x//2)
        return x//2
    elif x % 2 == 1:
        print(x*3+1)
        return 3*x + 1

if __name__ == '__main__':
    try:
        number = int(input('Enter a number: '))
        result = collatz(number)
        while(result != 1):
            result = collatz(result)
    except ValueError:
        print('must input an int')
