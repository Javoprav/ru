from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title
import os
import json
stud = os.path.join('data', 'students.json')
profi = os.path.join('data', 'professions.json')
student = ''

print('Введите номер студента: ')
user_input_pk = input()
print(get_student_by_pk(user_input_pk))

with open(stud, 'r', encoding='utf-8') as f:
    data3 = json.load(f)
    for i in data3:
        if i["pk"] == int(user_input_pk):
            student = i["full_name"]

user_input_prof = print(f'Выберите специальность для оценки студента {student}')





quit()