# coding=utf-8

def toString(charlist):
    return ''.join(charlist)

infile = open('/home/pau/Data/corpus/news.dat', 'rb')
outfile = open('/home/pau/Data/corpus/corpus.txt', 'w')
print(infile)
blankline = 0
while(True):# Ugly!!!!!!!!!! Should use for row in file
    if blankline > 100:
        break
    raw = infile.readline()
    if len(raw) == 0:
        blankline += 1
        continue
    if raw[:9] != b'<content>':
        blankline += 1
        continue
    blankline = 0
    raw = raw[9:]
    raw = raw[:-11]
    if len(raw) == 0:
        continue
    raw = raw.decode('GB18030')
    row = []
    for chara in raw:
        if '\u4e00' <= chara<='\u9fff':
            row.append(chara)
        else:
            if len(row) == 0:
                continue
            # print(toString(row))
            outfile.writelines(toString(row)+'\n')
            row = []
