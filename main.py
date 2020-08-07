print('Welcome')
Name = input('Enter your name')
age = int(input('Enter your age'))
print('Hello', Name, 'you are', age, 'years old')

if age >= 18:
    print('You are old enough to play!')
    Health = 5
    print('You have', Health, 'health')
    wanna_play = input('You want to play').lower()
    if wanna_play == 'yes':
        print('Lets start the game')

        left_or_right = input('Enter your choice either left or right')
        if left_or_right == 'right':
            go_on = input(
                'Now, you follow the path and you reach a lake.. do you swim across or go back?(across/go back) '
            )
            if go_on == 'across':
                carry_on = input(
                    'You know to swim good...but you got bit by a fish and lost a health'
                )
                print('You have', Health - 1, 'health')
                Health = Health - 1
                ans = input(
                    'You crossed the river and you notice a house and a thick forest..Where would you choose to go?(house/forest)'
                )
                if ans == 'house':
                    print(
                        'The house owner let you in and he apparently doesnt like you'
                    )

                    stay_or_left = input(
                        'Would you stay there or ask him to help you to return back?(stay/return)'
                    )
                    if stay_or_left == 'stay':
                        print(
                            'The house owner is a serial killer and now he is after you and now you know it think fast and do something'
                        )
                        print('You lost 2 health You have', Health - 2,
                              'health')
                        Health = Health - 2
                        thinking = input(
                            'What would you do to escape?(swim across/kill him)'
                        )
                        if thinking == 'swim across':
                            print(
                                'You are safe now and WON but on the way you again got bit by the fish so, you lost a health'
                            )
                            print('You have', Health - 1, 'health')
                            Health = Health - 1
                        else:
                            print('You just killed a man and you lost')

                    else:
                        print(
                            'You made a good choice and you WON but happen to lose 2 health'
                        )

                else:
                    print('A bear caught you and you lost!!')

            elif go_on == 'go back':
                print('You went back!! Bye')
            else:
                print('You lost')

        else:
            print('You fell down and lost')

    else:
        print('Bye')
elif age >= 14:
    print('You can play with supervision')
    superviser = input(
        'Do you have anyone older than you beside while you play(yes/no)')
    if superviser == 'yes':
        print('You can play')
        print('Lets start the game')
        Health = 5
        print('You have', Health, 'health')

        left_or_right = input('Enter your choice either left or right')
        if left_or_right == 'right':
            go_on = input(
                'Now, you follow the path and you reach a lake.. do you swim across or go back?(across/go back) '
            )
            if go_on == 'across':
                carry_on = input(
                    'You know to swim good...but you got bit by a fish and lost a health'
                )
                print('You have', Health - 1, 'health')
                Health = Health - 1
                ans = input(
                    'You crossed the river and you notice a house and a thick forest..Where would you choose to go?(house/forest)'
                )
                if ans == 'house':
                    print(
                        'The house owner let you in and he apparently doesnt like you'
                    )

                    stay_or_left = input(
                        'Would you stay there or ask him to help you to return back?(stay/return)'
                    )
                    if stay_or_left == 'stay':
                        print(
                            'The house owner is a serial killer and now he is after you and now you know it think fast and do something'
                        )
                        print('You lost 2 health You have', Health - 2,
                              'health')
                        Health = Health - 2
                        thinking = input(
                            'What would you do to escape?(swim across/kill him)'
                        )
                        if thinking == 'swim across':
                            print(
                                'You are safe now and WON but on the way you again got bit by the fish so, you lost a health'
                            )
                            print('You have', Health - 1, 'health')
                            Health = Health - 1
                        else:
                            print('You just killed a man and you lost')

                    else:
                        print(
                            'You made a good choice and you WON but happen to lose 2 health'
                        )

                else:
                    print('A bear caught you and you lost!!')

            elif go_on == 'go back':
                print('You went back!! Bye')
            else:
                print('You lost')

        else:
            print('You fell down and lost')

    else:
        print('You cant play')

else:
    print('You are not old enough to play')
