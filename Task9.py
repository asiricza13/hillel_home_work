"""Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати.
Користувач вводить число, а програма перевіряє його і, якщо користувач не вгадав,
що повідомляє ви введене число більше чи менше від згенерованого.
Після цього знову просить вгадати. І так, поки користувач не вгадає."""


import random
x = False
while x == False:
    number = int(input("Введіть ваше число:"))
    happy_number = random.randrange(1, 11)
    if number == happy_number:
        print("Пощастило!")
        x = True
    else:
        print("Спробуйте ще раз!", happy_number)