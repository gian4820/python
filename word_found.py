def search(text, word):
    count = 0
    texto = text.split()
    length = len(texto)
    for s in texto:
        if word == s:
            print ('Word found')
        else:
            count += 1
            if count == length :
                print ('Word not found')

    return text, word

text = input()
word = input()

search(text, word)

