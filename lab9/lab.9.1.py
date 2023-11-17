import pandas as pd
import matplotlib.pyplot as plt


# Завантаження даних
equipment_df = pd.read_csv('russia_losses_equipment.csv')
corrections_df = pd.read_csv('russia_losses_equipment_correction.csv')
personnel_df = pd.read_csv('russia_losses_personnel.csv')

# Попередня обробка даних
# Очистка від відсутніх значень та дублікатів (при необхідності)
equipment_df = equipment_df.dropna().drop_duplicates()
corrections_df = corrections_df.dropna().drop_duplicates()
personnel_df = personnel_df.dropna().drop_duplicates()

# Аналіз даних
# Розрахунок основних статистичних показників
equipment_stats = equipment_df.describe()

# Групування для аналізу підгруп у даних (при необхідності)
# Наприклад, групування по року
equipment_grouped_by_year = equipment_df.groupby('year').sum()

# Сортування даних (при необхідності)
# Наприклад, сортування за кількістю втраченої техніки
equipment_sorted = equipment_df.sort_values(by='tanks', ascending=False)

# Візуалізація даних
# Приклад візуалізації динаміки втрат танків
plt.figure(figsize=(10, 5))
plt.plot(equipment_df['date'], equipment_df['tanks'])
plt.xlabel('Дата')
plt.ylabel('Кількість втраченої техніки')
plt.title('Динаміка втрат танків')
plt.show()
