
x = 0
while x < 101:

    if x % 3 == 0 and x%5 != 0:
        print('fizz')
    elif x % 5 == 0 and x%3 != 0:
        print('buzz')
    elif x % 5 == 0 and x%3 == 0:
        print('fizzbuzz')
    else:
        print(x)
    x = x + 1
