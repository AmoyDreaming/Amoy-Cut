# coding=utf-8
import sqlite3
conn = sqlite3.connect('/home/pau/Data/dict.db')
file = open('/home/pau/Data/corpus/corpus.txt', 'r')
dictionary = {}
print('Arranging dictionary.')
cnt = 1000
for row in file:
    cnt -= 1
    if cnt == 0:
        break
    row = row[:-1]
    for i in range(len(row)):
        for j in range(len(row)-i):
            word = row[i:i+j+1]
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1
print('Inserting data into database.')
for key in dictionary.keys():
    conn.execute('INSERT INTO dict VALUES ("%s", %d, 0)' % (key, dictionary[key]))
conn.commit()