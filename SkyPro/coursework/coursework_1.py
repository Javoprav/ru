''' Импорт модуля Рандом'''

import random


"""Приветствие и запуск"""

print('Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем')
user_input_enter = input()
if user_input_enter == '':
    print('Начинаем!')
else:
    print('Запустите программу когда будете готовы!')
    quit()


"""вывод статистики"""

answers = []

def print_statistics(answers):
    total_tasks = 5
    answered_correctly = 0
    answered_incorrectly = 0
    for answer in answers:
        if answer == True:
            answered_correctly += 1
        else:
            answered_incorrectly += 1

    print(f'Всего задачек: {total_tasks}\nОтвечено верно: {answered_correctly} \nОтвечено неверно: {answered_incorrectly}')


"""Словарь Морзе"""
morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

"""Функция перевода слов Морзе"""

def morse_encode(word):
    translation = ''
    for letters in word:
        if letters in morse_dict:
            translation += morse_dict[letters] + ' '
    return translation

    # второй вариант
    '''translation = []
    for letters in word:
        translation.append(letters)
    return ' '.join(translation)'''

    # третий варинат
    '''return ' '.join([morse_dict[letters] for letters in word])'''


"""Список слов для игры"""

list_words = ['snake', 'little', 'code', 'bit', 'soul']
def get_word():
    items = random.sample(list_words, 1)
    result = ''.join(items)
    return result


"""Основной цикл с вопросами"""

game_cycle = 0
while game_cycle < 5:
    user_response_1 = get_word()
    user_response_1_morse = morse_encode(user_response_1)
    print(f"Переведите слово: {user_response_1_morse}")
    user_answer_1 = input().lower()
    if user_answer_1 == user_response_1:
        print('Ответ верный!')
        answers.append(True)
        game_cycle += 1
    else:
        print('Ответ не верный!')
        answers.append(False)
        game_cycle += 1

"""Вывод статистики"""

print_statistics(answers)



'''Семен Душкин
20.11.22 12:32
Привет, Максим!
Хорошо разобрался в теме, молодец)
Есть пара придирок:

1) Приводить ввод пользователя в нижнему регистру, так у него будет меньше вариантов на ошибку)

user_input = input().lower()
2) Сравнивать bool типы правильно через is, или можно использовать у списка функцию count()

if ans is True:
  pass
3) При написании кода, лучше придерживаться следующего стиля

импорты
константы
функции
выполняемый код
4) Закомментированный код лучше удалять
В остально всё хорошо, работа зачтена﻿😉﻿'''