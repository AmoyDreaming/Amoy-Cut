def load():
    file = open('../dict.txt', 'r')
    dictionary = {}
    while(True):
        row = file.readline().split(' ')
        if len(row) < 2:
            break
        dictionary[row[0]] = int(row[1])
    return dictionary

if __name__ == '__main__':
    load()