file = open("/Users/ggroppo/Documents/learn/python/books/books.txt", "r")

#your code goes here
line=file.readline()

while line:
    l=(line.strip())
    char=l[0]
    count=len(l)
    s=str(count)
    final= char + s
    print(final)
    line = file.readline() 



file.close()