def func1(func2):
    def func3(param):
        print("Computer")
        func2()
        print("Science")
@func1
def func2():
    print("Department")
func1()