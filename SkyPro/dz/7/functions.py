'''импорты и переменные'''
import os
import json
stud = os.path.join('data', 'students.json')
profi = os.path.join('data', 'professions.json')

'''Загружает список студентов из файла'''
def load_students():
    with open(stud, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    return data1

'''Загружает список профессий из файла'''
def load_professions():
    with open(profi, 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    return data2

'''Получает словарь с данными студента по его pk'''
def get_student_by_pk(pk):
    return_1 = ''
    with open(stud, 'r', encoding='utf-8') as f:
        data3 = json.load(f)
        for i in data3:
            if i["pk"] == int(pk):
                student = i["full_name"]
                skl = ' '.join(i["skills"])
                return_1 = f'Студент {student}\nЗнает {skl}'
            else:
                return_1 = 'У нас нет такого студента'

    return return_1

'''Получает словарь с инфо о профе по названию'''
def get_profession_by_title(title):
    with open(profi, 'r', encoding='utf-8') as f:
        data4 = json.load(f)
        for i in data4:
            if i["title"].lower() == title.lower():
                fitness = i["skills"]
                #student = i["full_name"]
                #skl = i["skills"]
    return f'{fitness}'

'''функция, которая получив студента и профессию, возвращает словарь'''
#def check_fitness(student, profession):