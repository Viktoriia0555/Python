import unittest
from random import choice

# Базові відповіді "чарівної кульки"
base_answers = ["Так", "Ні", "Можливо", "Спробуй пізніше", "Не маю впевнення"]


# Функція для конфігурації "чарівної кульки" з можливістю додавання відповідей
def configure_magic_ball(new_answers: list):
    global base_answers
    base_answers.extend(new_answers)


# Функція для визначення відповіді
def charivna_kulka(question):
    if not isinstance(question, str) or question == "":
        return "Питання не розпізнано"

    return choice(base_answers)


class TestCharivnaKulka(unittest.TestCase):
    def test_type_of_answer(self):
        self.assertIsInstance(charivna_kulka("Чи завтра буде сонячно?"), str)

    def test_answer_in_base_answers(self):
        self.assertIn(charivna_kulka("Чи завтра буде сонячно?"), base_answers)

    def test_empty_question(self):
        self.assertEqual(charivna_kulka(""), "Питання не розпізнано")

    def test_non_string_question(self):
        self.assertEqual(charivna_kulka(123), "Питання не розпізнано")


# Запуск тестів
# unittest.main()

# Приклад використання
configure_magic_ball(["Звісно", "Не можливо"])
print(charivna_kulka("Чи я виграю лотерею?"))