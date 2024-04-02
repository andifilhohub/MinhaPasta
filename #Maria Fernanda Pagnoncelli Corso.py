def index_joker(w):
    for i in range(len(w)):
        if w[i] == '*':
            return i
    
    

def same_words(word,text,id):
    frequency = 0 
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == word[0]:
                a = True
                for h in range(len(word)):
                    if h == id:
                        continue 
                    elif word[h] == text[i][j+h]:
                        continue
                    else: 
                        a = False
                        break
                if a:
                    frequency+=1
    return frequency
                    
                        


def main():
    much_row = int(input())
    text = []
    for i in range(much_row):
        text.append([input()])
    
    much_word = int(input())
    words = []
    for i in range(much_word):
        words.append(input())
        
    print(text)
    print(words)
    
main()
