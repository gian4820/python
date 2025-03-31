txt = input("Please add some text, and I'll find the longest word: ")
max=0
word=''
#your code goes here
s=txt.split()
for i in s:
    l=len(i)
    if l > max:
        max=l
        word=i
print(word)