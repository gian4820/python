names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]



    
def myFunc(x):
    if len(x) > 5:
        return True

new_names = filter(myFunc, names)

for x in new_names:
  print(x)