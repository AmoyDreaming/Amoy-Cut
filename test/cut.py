import load_dict
from sentence_tree import *

def process(parent, string):
    if len(string) == 0:
        return
    for i in range(len(string)):
        word = string[0:i+1]
        if word not in dictionary.keys():
            continue

        child = node(word, dictionary[word], parent)
        parent.next.append(child)
        process(child, string[i+1:])

    
def ergodic(p):
    score = 1000000000
    if len(p.next) == 0:
        return
    for child in p.next:
        if child.score < score:
            minchild = child
    print(minchild.value, '/', end=' ')
    ergodic(minchild)
    

if __name__ == '__main__':
    print('Loading dictionary.')
    dictionary = load_dict.load()
    print('Dictionary loaded.')

    while(True):
        sentence = input('Input your sentence: ')
        if sentence == 'exit':
            break

        head = node(None, 0, None)
        process(head, sentence)
        ergodic(head)
        print()
    