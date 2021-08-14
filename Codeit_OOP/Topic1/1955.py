# 데코레이터 함수
def add_print_to(original):
    def wrapper():
        print("Function Begin")
        original()
        print("Function End")
    return wrapper


@add_print_to
def print_hello():
    print("Hello World!")


print_hello()
