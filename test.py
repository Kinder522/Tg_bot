def my_first_decarator(function_to_decarator):
    # Создание функции
    def obertka_vokryg_ocnovnoi_function():
        print("Выполняем любые действия до функции")
        function_to_decarator()
        print("Выполняем любые действия после функции")

    return obertka_vokryg_ocnovnoi_function

def my_second_decarator(abc):
    def fn():
        print("Как по вашему где я окажусь?")
        abc()
        print("А этот текст где будет?")
    return fn


@my_first_decarator
@my_second_decarator
def function():
    print("Текст в основной функции!")

function() 
