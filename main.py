# Завдання 1

from queue import Queue
import random
# Створити чергу заявок
queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

def generate_request ():
    new_request = random.randint(1, 5)
    queue.put(new_request)
    print(f"Додана заявка {new_request}")

# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

def  process_request():
    if queue.empty():
        print("черга пуста")
    else:
        services_request = queue.get()
        print(f"Оброблена заявка {services_request}")

i = 0
while i <=5:
    generate_request ()
    i +=1

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок

def main():
    while True:
        # Генеруємо нову заявку
        generate_request()

        # Обробляємо заявку
        process_request()

        # Запитуємо користувача, чи хоче він продовжити
        user_input = input("Продовжити? (так/вийти): ").strip().lower()
        if user_input == "вийти":
            print("Завершення програми...")
            print(f"Маємо чергу {list(queue.queue)}")
            break

if __name__ == "__main__":
    main()


# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

from collections import deque

def check_polindrom(sentense):
    perem = deque(sentense.replace(' ', '').casefold().strip())
    if perem:
        print("succesful")
        if len(perem)%2 != 0:
            return (print("It's not a polindrom. The length is odd"))
        else:
            while len(perem) != 0:
                start_data = perem.pop()
                end_data = perem.popleft()
                if start_data != end_data:
                    return (print("It's not a polindrom. The length is odd"))
                else:
                    continue
            return (print(f'{sentense} is polindrom'))
    else:
        print("correct your sentense")


def main():
    check_polindrom("Abbbb bba")

if __name__ == "__main__":
    main()

# Завдання 3 (необов'язкове завдання)

# У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, такими як круглі ( ), квадратні [ ] або фігурні дужки { }.
# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.

def checkSymbols(option):
    keys_pattern = {"{": "}", "[": "]", "(": ")"}
    
    # Використовуємо стек для перевірки збалансованості дужок
    stack = []
    
    for char in option:
        if char in keys_pattern:  # якщо символ - відкрита дужка
            stack.append(char)  # додаємо його в стек
        elif char in keys_pattern.values():  # якщо символ - закрита дужка
            if stack and keys_pattern[stack[-1]] == char:  # перевіряємо, чи є відповідна відкрита дужка в стеці
                stack.pop()  # видаляємо пару з стеку
            else:
                return print("Несиметрично")  # не знайдено відповідної пари, несиметрично

    if stack:
        return print("Несиметрично")  # залишаються не закриті дужки в стеці, несиметрично
    return print("Симетрично")  # стек порожній, всі дужки співпали

def main():
    # Тестування
    checkSymbols("( ){[ 1 ]( 1 + 3 )( ){ }}")  # Симетрично
    checkSymbols("( 23 ( 2 - 3)")  # Несиметрично
    checkSymbols("( 11 }")  # Несиметрично

if __name__ == "__main__":
    main()


def main():
    checkSymbols("( ){[ 1 ]( 1 + 3 )( ){ }}")
    checkSymbols("( 23 ( 2 - 3)")
    checkSymbols("( 11 }")
