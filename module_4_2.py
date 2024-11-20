def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"
    a = inner_function()
    print(a)
test_function() # выводит Я в области видимости функции test_function
inner_function() # выводит ошибку, так как не видит функцию inner_function

