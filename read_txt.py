pd = open ("/home/gian/Documents/rundeck/gian/txt/pd.txt", "r")
#the r mean that we will read the file

#read all the file
print(pd.read())

#read only one line, the first
print(pd.readline())

#read only one line, the second
print(pd.readline())

#we always have to close the file
pd.close()