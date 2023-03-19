money = int(input('введите сумму, которую планируете вложить '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = []

for key in per_cent:
    deposit.append(money * per_cent[key] * 100)

deposit_i = max(deposit)
print(deposit)

print('Максимальная сумма, которую вы можете заработать ' + str(deposit_i))


