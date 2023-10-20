import csv
import pandas as pd


header = ["Марка", "Модель", "Рік", "Колір"]
with open("база_даних_автомобілів.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)


cars_data = [
    ["Porsche", "Cayenne", 2019, "Срібний"],
    ["Porsche", "Macan", 2020, "Чорний"],
    ["Land Rover", "Discovery", 2017, "Синій"],
    ["BMW", "X7", 2023, "Сірий"],
    ["Lexus", "RX", 2021, "Білий"],
]

with open("база_даних_автомобілів.csv", "a", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(cars_data)


with open("база_даних_автомобілів.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(", ".join(row))


year_to_search = 2019
with open("база_даних_автомобілів.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропускаємо заголовок
    for row in csv_reader:
        if int(row[2]) == year_to_search:
            print(", ".join(row))


car_to_update = "Porsche"
new_color = "Рожевий"

with open("база_даних_автомобілів.csv", "r") as file:
    rows = list(csv.reader(file))

for row in rows:
    if row[0] == car_to_update:
        row[3] = new_color

with open("база_даних_автомобілів.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([header] + rows)


car_to_delete = "Porsche"
model_to_delete = "Macan"

with open("база_даних_автомобілів.csv", "r") as file:
    rows = list(csv.reader(file))

new_rows = [header]
for row in rows:
    if row[0] != car_to_delete or row[1] != model_to_delete:
        new_rows.append(row)

with open("база_даних_автомобілів.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(new_rows)


df = pd.read_csv("база_даних_автомобілів.csv")
brand_avg_year = df.groupby("Марка")["Рік"].mean().reset_index()
print("\nСередній рік випуску для кожної марки:")
print(brand_avg_year)