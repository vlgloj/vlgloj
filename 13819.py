tickets = int(input("Введите количество билетов:"))
N = 0
bill = 0
buyers = []
while N < tickets:
    N = N + 1
    age = int(input("Введите возраст:"))
    if age < 18:
        buyers.append(int(bill))
    if 18 <= age <= 25:
        bill = 990
        buyers.append(int(bill))
    if age > 25:
        bill = 1390
        buyers.append(int(bill))
if tickets <= 3:
    print("Сумма стоимости билетов:", sum(buyers))
else:
    print ("Сумма стоимости билетов:", int((sum(buyers)*0.9)))
