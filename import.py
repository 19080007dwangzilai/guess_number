import random

start = input('enter the first num:')
end = input('enter the last num:')
r = random.randint(int(start), int(end))
count = 10
while count > 0:
    count -= 1
    answer = int(input('enter your guess num:'))
    if answer == r:
        print('guess right!')
        print('you have guessed', 10 - count, 'times')
        break
    else:
        if count > 0:
            print('you still have', count, 'times')
            if answer > r:
                print('your guess is bigger than r')
            elif answer < r:
                print('your guess is smaller than r')
        elif count == 0:
            print('game over')
