import time

def main():
    print("Ласкаво просимо до гри!")
    print("Ви стоїте перед великим замком.")
    print("Виберіть, куди ви хочите зайти перше:\n1. Зайти через ворота.\n2. Зайти через двері.")
   

    choice = input("Ваш вибір (1/2): ")

    if choice == '1':
        option_left()
    elif choice == '2':
        option_right()
    else:
        print("Невірний вибір. Гра завершена.")

def option_left():
    print("Ви вирушили в середину замку.")
    time.sleep(2)
    print("Замок стає дуже довгий, і ви загубилися.")
    time.sleep(2)
    print("Виберіть, що ви хочете зробити:\n1. Спробувати знайти дорогу назад.\n2. Продовжити рухатися вперед.")


    choice = input("Ваш вибір (1/2): ")

    if choice == '1':
        print("Ви намагалися знайти дорогу назад, але загубились ще більше. Гра закінчена.")
    elif choice == '2':
        print("Ви продовжили рухатися вперед і натрапили на старовинний сховок. Ви виграли!")
    else:
        print("Вибір недопустимий. Гра завершена.")

def option_right():
    print("Ви рушаєте далі в глиб замку.")
    time.sleep(2)
    print("Під час свого подорожі ви знаходите золотий ключ.")
    time.sleep(2)
    print("Виберіть, що ви хочете зробити з ключем:\n1. Використовувати ключ і відкрити сейф, який лежить біля загадкових дверей.\n2. Ігнорувати ключ і продовжити рухатися вперед.")

    choice = input("Ваш вибір (1/2): ")

    if choice == '1':
        print("Ви відкрили сейф і знайшли в ньому скарб. Ви виграли!")
    elif choice == '2':
        print("Ви продовжили свою подорож, але не знайшли нічого цікавого. Гра закінчена.")
    else:
        print("Вибір недопустимий. Гра завершена.")

if __name__ == "__main__":
    main()