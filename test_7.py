import csv
import random


def row_gen(types):
    row = []
    for data_type in types:
        if data_type == int:
            row.append(random.randint(1, 100))
        elif data_type == str:
            row.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for x in range(random.randint(1, 99))))
        elif data_type == bool:
            row.append(random.choice([True, False]))
        else:
            raise ValueError("Неверный тип")
    return row


def csv_gen(N, header: dict):
    assert N <= 10 ** 9, 'Много строк'
    assert header != dict(), "Заголовок должен быть"
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header.keys())
        for i in range(N):
            writer.writerow(row_gen(header.values()))
