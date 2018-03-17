#-*- coding: utf-8 -*-
""" Обрабатывает файл и создает частотный словарь (частота повторения слова в тексте) """

import sys
import os
import re

if len(sys.argv) == 1:
    print('Нет параметров для запуска!\n\n   Пример  $ python count2.py some_file.txt\n')
    sys.exit(1)

input_file = sys.argv[1]
if os.path.isfile(input_file):
    print('Рабочий файл: ' + input_file)

# читаем файл
file = open(input_file, 'r')
try:
    txt = file.read()
finally:
    file.close()

# выбираем слова через регулярные выражения
p = re.compile("([a-zA-Z-']+)")
res = p.findall(txt)

# создаем словарь. Ключ-слово, Значение-частота повторения
lsWord = {}
for key in res:
    key = key.lower()
    if key in lsWord:
        value = lsWord[key]
        lsWord[key] = value + 1
    else:
        lsWord[key] = 1

# создаем список ключей отсортированный по значению словаря lsWord
sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
print sorted_keys



file = open(input_file + '_dict.csv', 'a+')
try:
    for key in sorted_keys:
        s = str(lsWord[key]) + ' ' + str(key) + '\n'
        file.writelines(s)
    print('Резуьтат записан: ' + input_file + '_dict.csv')
finally:
    file.close()
