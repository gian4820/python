from copyreg import constructor


friends = ["Pedro", "Armando", "Julio", "Augusto", "Juan"]
fav_nums = [1, 10, 5, 7, 9, 4]

#seleccionas elemento 3
print("")
print("SELECCIONAMOS ELEMENT")
print("Seleccionamos el elemento 3 = "  + friends[3])

#extends, incrementa el array
print("")
print("EXTEND")
friends.extend(fav_nums)
print (friends)

#append
print("")
print("APPEND")
friends.append("Pablo")
print(friends)

#insert
print("")
print("INSERT")
friends.insert(3, "Marcos") 
print (friends)

#remove
print("")
print("REMOVE")
friends.remove("Pablo")
print(friends)

#clear
print("")
print("CLEAR")
#friends.clear()

#pop
print("")
print("POP")
friends.pop()
print(friends)

#index
print("")
print("INDEX")
print(friends.index("Julio"))

#sort
print("")
print("SORT")
fav_nums.sort()
print(fav_nums)

#reverse
print("")
print("REVERSE")
fav_nums.reverse()
print(fav_nums)

#copy
print("")
print("COPY")
friends2 = friends.copy()
print(friends2)