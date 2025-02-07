"""Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая
из модуля hashlib)"""


def count_substring(s: str) -> int:
    hash_set = set()
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            hash_set.add(hash(s[i:j]))
    return len(hash_set) - 1


test_str = input("Введите строку для проверки на подстроки: ")
print(f"В строке {test_str} есть {count_substring(test_str)} подстрок")
