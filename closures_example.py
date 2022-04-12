
def outer(name):
    # this is the enclosing function

    def inner():
        # this is the enclosed function

        # the inner function accessing the outer function's variable 'name'
        print(name)
    inner()


# call the enclosing function
outer('tejalmulik')

