import sys
def my_function(fname, lname):
    print("My full name is:")
    print(fname + " " + lname)

my_function(sys.argv[1], sys.argv[2])