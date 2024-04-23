print("Name: Ansh\nRoll No: 2210997036")
def argument(*args, **kwargs):
    print("Positional Arguments: ")
    for arg in args:
        print(arg)
    print("Keywords Arguments: ")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
argument(1,2,3, name= "Dhruv", age= 19)
