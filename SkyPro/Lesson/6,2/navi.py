'''Навигация
Пути при работе с файлами совпадают с теми, которые вы используете при работе с терминалом. Напомним, как они работают:
/
Путь от корня
./
Текущая папка
cat
Вложенная папка
../
Родительская папка
Вот небольшая таблица, которая показывает, как работает навигация по файловому дереву:'''
import os
open("data.txt")
os.path.join("data.txt")
# Открыть файл в папке, где выполняется код
open("./data.txt")
os.path.join(".", "data.txt")
# То же самое
open("cat/data.txt")
os.path.join("cat", "data.txt")
# Зайти в папку cat, открыть файл
open("../data.txt")
os.path.join("..", "data.txt")
# Подняться на уровень выше и открыть файл
open("../cat/data.txt")
os.path.join("..", "cat", "data.txt")
# Подняться выше, зайти в папку cat, открыть файл
open("/data.txt")
os.path.join("/", "data.txt")
# Зайти в корневую папку, открыть в ней файл

'''Проверка существования
Иногда бывает полезно проверить существование файла перед чтением (чтобы не вызвать ошибку) или, наоборот, перед его перезаписью (чтобы случайно его не перезаписать и не потерять данные). Тогда нам пригодится 
os.path.exists(<путь>)
, который работает как с папками, так и с файлами.
Например:
'''
# Для файла

if os.path.exists("data.txt"):
	print("Файл существует")
else:
	print("Файл не существует")
# Для папки

if os.path.exists("data"):
	print("Папка существует")
else:
	print("Папка не существует")

'''Абсолютный путь
Хотя Python без проблем считает свои пути от той директории, в которой он находится, иногда нам нужно получить полный путь от корня, который обычно называют 
root
. Для Windows-подобных систем это один их физических дисков, например 
С:\\
. А для UNIX-подобных — корневая папка, у которой нет имени.
Чтобы перейти в эту папку, в терминале нам нужно написать:
В UNIX-подобных
В Windows
cd /
cd \
Например, наш скрипт находится внутри папки 
sample, внутри папки lesson_6
Чтобы узнать, какой путь от корня до папки, где находится наша программа, нам нужно написать в нашем Python-файле:'''
print(os.path.abspath("."))
# // или, что то же самое
print(os.path.abspath("."))
'''Абсолютный Путь От Относительного Пути
Используйте os.path.abspath :'''
 >>> os.getcwd()
'/Users/csaftoiu/tmp'
>>> os.path.abspath('foo')
'/Users/csaftoiu/tmp/foo'
>>> os.path.abspath('../foo')
'/Users/csaftoiu/foo'
>>> os.path.abspath('/foo')
'/foo' 


open("/data.txt")	
# Откроет файл в корневой папке

'''тобы отделить один компонент от пути:'''

 >>> p = os.path.join(os.getcwd(), 'foo.txt')
>>> p
'/Users/csaftoiu/tmp/foo.txt'
>>> os.path.dirname(p)
'/Users/csaftoiu/tmp'
>>> os.path.basename(p)
'foo.txt'
>>> os.path.split(os.getcwd())
('/Users/csaftoiu/tmp', 'foo.txt')
>>> os.path.splitext(os.path.basename(p))
('foo', '.txt') 

'''Получить родительский каталог'''
 os.path.abspath(os.path.join(PATH_TO_GET_THE_PARENT, os.pardir)) 

'''Если данный путь существует.
проверить, существует ли данный путь'''

path = '/home/john/temp'
os.path.exists(path)

'''проверьте, является ли данный путь каталогом, файлом, символической ссылкой, точкой монтирования и т. д.
проверить, является ли данный путь каталогом'''

 dirname = '/home/john/python'
os.path.isdir(dirname)

# проверить, является ли данный путь файлом

 filename = dirname + 'main.py'
os.path.isfile(filename)

# чтобы проверить , если данный путь является символической ссылкой

 symlink = dirname + 'some_sym_link'
os.path.islink(symlink)

# чтобы проверить , если данный путь является точка монтирования

 mount_path = '/home'
os.path.ismount(mount_path) 

import os
(os.remove('d:/file.txt')) # удаление файла

import os
(os.makedirs('d:/file.txt')) # создание файла

import os
(os.makedirs('d:/dir')) # создание папки

import shutil
(shutil.rmtree('d:/dir')) # удаление папки

import os
(os.startfile('d:/file.txt')) # запуск файла