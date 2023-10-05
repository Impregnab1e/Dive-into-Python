# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления 
# и снятия средств в список.

s = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600
operations_history = []


def apply_rich_tax(balance):
    if balance >= RICHLIMIT:
        return balance * RICHTAX
    return balance


def apply_bonus(balance, count):
    if count % THREEOPERATIONS == 0 and count != 0:
        return balance * BONUSTHREE
    return balance


def deposit(balance, amount):
    if amount % FREENDERING == 0:
        return balance + amount
    return balance


def withdraw(balance, amount):
    if amount % FREENDERING == 0:
        commission = amount * COMMISSIONOUTDROW
        if commission < MINLIMIT:
            commission = MINLIMIT
        elif commission > MAXLIMIT:
            commission = MAXLIMIT
        if (commission + amount) < balance:
            return balance - (amount + commission)
    return balance


while True:
    action = input('Введите операцию 1,2,3: ')
    if action == '1':
        withdrow = int(input('Введите сумму: '))
        s = deposit(s, withdrow)
        operations_history.append(f"Пополнение: +{withdrow}")
    elif action == '2':
        withdrow = int(input('Введите сумму: '))
        s = withdraw(s, withdrow)
        operations_history.append(f"Снятие: -{withdrow}")
    else:
        break
    s = apply_rich_tax(s)
    s = apply_bonus(s, count)
    count += 1
    print(f"Баланс: {s}")
