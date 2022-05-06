money = int(input('Введите сумму:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
TKB = money / 100 * per_cent['ТКБ']
SKB = money / 100 * per_cent['СКБ']
VTB = money / 100 * per_cent['ВТБ']
SBER = money / 100 * per_cent['СБЕР']
deposit.append(int(TKB))
deposit.append(int(SKB))
deposit.append(int(VTB))
deposit.append(int(SBER))
depositmax = max(deposit)
print('Максимальная сумма, которую вы можете заработать — ', depositmax , ('монет за год.'))