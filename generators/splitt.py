txt = input()

def words():
    #your code goes here
    sep=txt.split()
    for i in sep:
        yield i

print(list(words()))
