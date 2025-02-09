from typing import Callable, Any
from functools import wraps

def password_checker_decorator() -> Callable:
    """
    **Критерии проверки пароля**:
	- Минимальная длина: 8 символов.
	- Содержит хотя бы одну цифру.
	- Содержит хотя бы одну заглавную букву.
	- Содержит хотя бы одну строчную букву.
	- Содержит хотя бы один специальный символ
    **Поведение**: Если пароль соответствует всем условиям, декоратор вызывает оригинальную функцию. В противном случае возвращает сообщение об ошибке.
    
    """
    def decorator(func: Callable) -> Callable:       
        def wrapper (pswrd:str) -> Any:
            correct_check:list = [0, 0, 0, 0]
            if len(pswrd) >= 8:
                for symbol in pswrd:
                    if symbol.isnumeric():
                        correct_check[0] = 1
                    elif symbol.isupper():
                        correct_check[1] = 1
                    elif symbol.islower():
                        correct_check[2] = 1
                    elif symbol in ".,:;!_*-+()/#¤%&~?<>[]@$^*":
                        correct_check[3] = 1     
            if  0 in correct_check:
                print(f' Длина вашего пароля менее 8 символов, либо он не содержит: \n - хотя бы одну цифру \n - хотя бы одну заглавную букву \n - хотя бы одну строчную букву \n - хотя бы один специальный символ (например, .,:;!_*-+()/#¤%&~?<>[]@$^*)')                
            else:
                return func(pswrd)
        return wrapper
    return decorator

@password_checker_decorator()
def register_user(pswrd:str) -> bool:
    """
    - **Аргументы**: Принимает пароль в качестве аргумента.
	- **Возвращаемое значение**: 
        Сообщение об успешной регистрации, если пароль прошел проверку, is_registered = True
        или сообщение об ошибке в противном случае.

    """
    is_registered:bool = True
    print (f'Регистрация прошла успешно!')
    return is_registered

print('-------------1------------')
print('Для пароля 1')
print(register_user("1qaz!QAZ"))
print('Для пароля 2')
print(register_user("qaz!QAZ"))
print('Для пароля 3')
print(register_user("1qazQAZ"))
print('Для пароля 4')
print(register_user("1qaz!"))
print('Для пароля 5')
print(register_user("1!QAZ"))

print('-------------2------------')
import csv

def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1): 
    """
    **Декоратор `password_validator`**
    - **Параметры**:
    - `min_length`: Минимальная длина пароля (по умолчанию 8).
    - `min_uppercase`: Минимальное количество заглавных букв (по умолчанию 1).
    - `min_lowercase`: Минимальное количество строчных букв (по умолчанию 1).
    - `min_special_chars`: Минимальное количество специальных символов (по умолчанию 1).
    - **Функциональность**:
    - Проверяет, соответствует ли пароль заданным критериям.
    - Если пароль не соответствует, выбрасывает `ValueError` с описанием проблемы.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper (username: str, password: str) -> Any:
            correct_check:list = [0, 0, 0]
            if len(password) >= length:
                for symbol in password:
                    if symbol.isupper():
                        correct_check[0] += 1
                    elif symbol.islower():
                        correct_check[1] += 1
                    elif symbol in ".,:;!_*-+()/#¤%&~?<>[]@$^*":
                        correct_check[2] += 1
                if  correct_check[0] < uppercase or correct_check[1] < lowercase or correct_check[2] < special_chars:
                    print(f' Длина вашего пароля не сответсвует заданным условиям') 
                    raise ValueError(f' Ошибка регистрации, пароль не прошел проверку')               
                else:
                    return func(username, password)
        return wrapper
    return decorator
    

def username_validator():    
    """
    **Декоратор `username_validator`**
    - **Функциональность**:
    - Проверяет, что в имени пользователя отсутствуют пробелы.
    - Если в имени пользователя есть пробелы, выбрасывает `ValueError` с описанием проблемы.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper (username: str, password: str) -> Any:
            
            if ' ' in username:
                raise ValueError(f' В имени пользователя не должно быть пробелов')                
            else:
                    return func(username, password)
        return wrapper
    return decorator

@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
@username_validator()
def register_user(username: str, password: str) -> bool:
    """
    - **Аргументы**: Принимает `username` и `password`.
    - **Функциональность**:    
    - Дозаписывает имя пользователя и пароль в **CSV файл**.
    - **возвращает при корректной регистрации**: is_registered = True
    """
    # if
    with open('CSV-file.csv', "a", encoding='UTF-8') as file:    
        writer = csv.writer(file, delimiter=';', lineterminator="\n" )
        data = [username, password]
        writer.writerow(data)
        print("====Файл CSV дозаписан")
    is_registered:bool = True    
    return is_registered

print('Тестирование успешного случая')
try:
    register_user("JohnDoe", "PPassword123@!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

print('-----')
print('Тестирование неудачного случая по паролю...')
try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

print('-----')
print('Тестирование неудачного случая по юзернейму...')
try:
    register_user("John Doe", "PPassword123!@")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")