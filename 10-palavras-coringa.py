def danizika(word,text):
    index = []
    letter,frequency,occurrence = 0,0,0
    for i in range(len(word)):
        if word[i] == '*':
            index.append(int(i))
    h = 0
    for i in range(len(text[0])):
        lenght = 0
        while text[i] != ' ':    
            if h > len(word)-1:
                continue
            elif text[0][i] == word[h] or word[h] == '*':
                letter+=1
                h+=1
            lenght+=1
            
        if letter == len(word) and lenght == len(word):
            occurrence+=1
        elif letter == len(word) and lenght != len(word):
            frequency+=1
            

def main():
    text = []
    number_row = int(input())
    for i in range(number_row):
        text.append(input())
    number_words = int(input())
    words = []
        
    for i in range(number_words):
        words.append(input())

    
    
main()