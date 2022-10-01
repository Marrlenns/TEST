while True:
    n1 = float (input('введите первое число - '))
    action = input('введите действие - ')
    n2 = float (input('введите второе число - '))

    if action == '+':
        ans = n1 + n2
        print(ans)
    elif action == '-':
        ans = n1 + n2
        print(ans)
    elif action == '*':
        ans = n1 * n2
        print(ans)

    elif action == '/' and n2 == 0:
        print ('на ноль делить нельзя')

    elif action == '/':
        ans = n1 / n2
        print(ans)
    else:
        print('так нельзя')

