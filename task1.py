# Монетки. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной.

import random


def FillList(n, listCoins):
    for i in range(n):
        listCoins.append(random.randint(0, 1))
    return listCoins


def FindCoins(n, listCoins, count):
    for i in range(n):
        if listCoins[i] == 0:
            count += 1
    return count


numberCoins = int(input('Введите число монет: '))
listCoins = list()
count = 0
print(FillList(numberCoins, listCoins))
print(f'Перевернуть нужно: {FindCoins(numberCoins, listCoins, count)}')
