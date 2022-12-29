def func1(func2):
    def func3():
        print("Computer")
        func2()
        print("Science")
    return func3
@func1
def func2():
    print("Department")
func2()