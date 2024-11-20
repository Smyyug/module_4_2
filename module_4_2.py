def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"
    a = inner_function()
    print(a)
test_function()
inner_function()

