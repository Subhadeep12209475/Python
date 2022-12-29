def trace(fn):
    def wrapped(x):
        return fn(x)
    return wrapped
@trace
def fn(x):
    return 3*x
print(fn(3))