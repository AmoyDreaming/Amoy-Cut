import load_dict
from sentence_tree import *

def process_asc(parent, string):
    if len(string) == 0:
        return
    for i in range(len(string)):
        word = string[:i+1]
        if word not in dictionary.keys():
            continue
        child = node(word, dictionary[word], parent)
        parent.next.append(child)
        process_asc(child, string[i+1:])


def process_desc(parent, string):
    l = len(string)
    if l == 0:
        return
    for i in range(len(string)):
        word = string[l-i-1:]
        if word not in dictionary.keys():
            continue
        child = node(word, dictionary[word], parent)
        parent.next.append(child)
        process_desc(child, string[:l-i-1])


def ergodic_asc(p, scoresum):
    score = 1000000000
    if len(p.next) == 0:
        return scoresum
    for child in p.next:
        if child.score < score:
            minchild = child
    print(minchild.value, '/', end=' ')
    scoresum += minchild.score
    return ergodic_asc(minchild, scoresum)


def ergodic_desc(p, scoresum):
    score = 1000000000
    if len(p.next) == 0:
        return scoresum
    for child in p.next:
        if child.score < score:
            minchild = child
    result.append(minchild.value)
    scoresum += minchild.score
    return ergodic_desc(minchild, scoresum)
    

if __name__ == '__main__':
    print('Loading dictionary.')
    dictionary = load_dict.load()
    print('Dictionary loaded.')

    while(True):
        sentence = input('Input your sentence: ')
        if sentence == 'exit':
            break

        head_asc = node(None, 0, None)
        process_asc(head_asc, sentence)
        print('Greedy Asc:  ', end='')
        score = ergodic_asc(head_asc, 0)
        print(' Score', score)

        result = []
        head_desc = node(None, 0, None)
        process_desc(head_desc, sentence)
        print('Greedy Desc: ', end='')
        score = ergodic_desc(head_desc, 0)
        l = len(result)
        for i in range(l):
            print(result[l-i-1], '/', end=' ')
        print(' Score', score)
