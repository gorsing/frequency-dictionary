#-*- coding: utf-8 -*-
""" Обрабатывает файл и создает частотный словарь (частота повторения слова в тексте) """

import sys
import os
import re

if len(sys.argv) == 1:
    print('Нет параметров для запуска!')
    sys.exit(1)

work_file = sys.argv[1]
if os.path.isfile(work_file):
    print('Рабочий файл: ' + work_file)

# читаем файл
file = open(work_file, 'r')
try:
    txt = file.read()
finally:
    file.close()

# выбираем слова через регулярные выражения
p = re.compile("([a-zA-Z-']+)")
res = p.findall(txt)

#print res[2]
slov = []
group_world = '', '', '', ''
print group_world
for i in range(len(res)):
    res[i].lower()
    if res[i] in group_world:
        slov.append(res[i + 1])
        #res[i]=res[i-1]
    #print slov

lsWord = {}

for i in range(len(slov)):
    slov[i].lower()
    if slov[i] in lsWord:
        value = lsWord[slov[i]]
        lsWord[slov[i]] = value + 1
    else:
        lsWord[slov[i]] = 1

#print lsWord

# создаем список ключей отсортированный по значению словаря lsWord
sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
#print '++++++++++++++++++++++++++++++++++++'
#print sorted_keys

file = open(work_file + '_dict.csv', 'a+')
try:
    for key in sorted_keys:
        s = str(lsWord[key]) + ' ' + str(key) + '\n'
        file.writelines(s)
    print('Резуьтат записан: ' + work_file + '_dict.csv')
finally:
    file.close()
