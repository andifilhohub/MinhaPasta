def index_joker(w):
    for i in range(len(w)):
        if w[i] == '*':
            return i
    
    

def same_words(word,text,id):
    frequency = 0 
    a = True
    for i in range(len(text)):
        for j in range(text[i]):
            if j == id:
                continue
            elif word[j] == text[i][j]:
                continue
            else: a = False
        if a and len(word) == len(text[i]):
            frequency+=1
        
    return frequency
                
    
    return frequency
def word_separator(List):
    newList = []
    word = []
    for i in range(len(List)):
        if List[i] == ' ':
            if ',' in word:
                word.remove(',')
                newList.append([''.join(str(number) for number in word)])
            elif '.' in word:
                word.remove('.')
                newList.append([''.join(str(number) for number in word)])
            else:
                newList.append([''.join(str(number) for number in word)])
            
            word = []
        else: word.append(List[i])
    if ',' in word:
        word.remove(',')
        newList.append([''.join(str(number) for number in word)])
    elif'.' in word:
        word.remove('.')
        newList.append([''.join(str(number) for number in word)])
    else:
        newList.append([''.join(str(number) for number in word)])
    return newList
                        


def main():
    much_row = int(input())
    text = []
    for i in range(much_row):
        text.append([input().lower()])
    
    much_word = int(input())
    words = []
    for i in range(much_word):
        words.append(input().lower())
    print(word_separator(text[3][0]))
    
main()
    