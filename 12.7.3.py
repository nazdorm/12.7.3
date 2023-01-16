money = int(input("Какую сумму планируете положить под проценты?"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
deposit.append(money/100*per_cent['ТКБ'])
deposit.append(money/100*per_cent['СКБ'])
deposit.append(money/100*per_cent['ВТБ'])
deposit.append(money/100*per_cent['СБЕР'])
print("Максимальная сумма, которую вы можете заработать", max(deposit))