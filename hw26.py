from typing import Callable, Any
from functools import wraps
import sys
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