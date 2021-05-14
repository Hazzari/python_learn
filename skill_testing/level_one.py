import re
import string as st
from collections import defaultdict

data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35,
        48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20,
        18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1,
        11, 21, 1, 44, 24, 42, 42, 41, 14, 24]


# 1. Вывести список уникальных чисел (встречаются только один раз)
# Два варианта решения:


def dict_values_output(d):
    """Вывод значений в консоль."""
    for key, value in d.items():
        if value == 1:
            print(f'Значение {key} уникально')
    print("*" * 10)


# 1 - Метод с библиотекой collection
all_numbers_count_dd = defaultdict(int)

for val in data:
    all_numbers_count_dd[val] += 1

# dict_values_output(all_numbers_count_dd)

# 2 - Метод со стандартным словарем
regular_dictionary = {}

for val in data:
    if val in regular_dictionary:
        regular_dictionary[val] += 1
    else:
        regular_dictionary[val] = 1

# dict_values_output(regular_dictionary)


# 2. Вывести список чисел <= 40, не встречающихся в исходном списке
# Вариант с обычным for
missing_value = []
for val in range(41):
    if val not in set(data):
        missing_value.append(val)
# print(missing_value)

# Однострочный вариант через list comprehension:
missing_value_comp = [_ for _ in range(41) if _ not in [_ for _ in set(data) if _ <= 40]]
# print(missing_value_comp)


# 3. Вывести данные в формате
# (num: num_count),
# (num: num_count),
# num_count - кол-во num в списке.
# Отсортировать по убыванию num_count, при равенстве num_count по убыванию num.

tuple_of_values = sorted(
        [(k, v) for k, v in all_numbers_count_dd.items()],
        key=lambda sort_key: (sort_key[1], sort_key[0]))

for val in tuple_of_values:
    # print(f'({x[0]}: {x[1]}),')
    pass

# 4. Рассчитать среднеквадратичное отклонение.

# print(stdev([n[1] for n in tuple_of_values]))

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipE' \
       'UlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAH' \
       'qnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFU' \
       'zxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWj' \
       'UeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaO' \
       'nLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunur' \
       'ZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKn' \
       'VJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc '

# 5. Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.

# Решить задачу двумя способами: с помощью re и без.

pattern_one = f'(?<=[A-Z])[a-z](?=[A-Z])'

substring_array = re.findall(pattern_one, line)
#
# print(f'Вариант с re: {substring_array}')

result = []
for val in enumerate(line):
    try:
        prefix = line[val[0] - 1]
        suffix = line[val[0] + 1]
        if val[1] in st.ascii_lowercase and line[val[0] - 1] in st.ascii_uppercase and suffix in st.ascii_uppercase:
            result.append(f'{val[1]}')
    except IndexError:
        break

# print(f'Вариант без re: {result}')

# 6. Вывести символы в верхнем регистре,
# которые окружают ровно два символа в нижнем регистре слева и два символа в верхнем регистре справа.
# Решить задачу двумя способами: с помощью re и без.

pattern_two = '(?<=[a-z][a-z])[A-Z](?=[A-Z][A-Z])'
substring_array = re.findall(pattern_two, line)
# print(substring_array)

result = []
for val in enumerate(line):
    if val[0] < 1:
        continue
    try:
        if val[1] in st.ascii_uppercase:
            if line[val[0] - 1] in st.ascii_lowercase and line[val[0] - 2] in st.ascii_lowercase and \
                    line[val[0] + 1] in st.ascii_uppercase and line[val[0] + 2] in st.ascii_uppercase:
                result.append(f'{val[1]}')
    except IndexError:
        break

# print(result)
# 7. Записать исходную строку в 5 разных файлов (1-й символ в первый, второй во второй и т.д.),
# имеющих названия 'file_1', 'file_2' и т.д.


# Записать в файл

for char in enumerate(line):
    count_file = 4
    if char[0] <= count_file:
        file_name = f'file_{char[0] + 1}.txt'

        with open(file_name, mode='w', encoding='utf8') as file:
            file.write(f'{char[1]}')
            file.writelines(line)


# 8. Вывести числа от 1 до 100 включительно. Если число делится на 3 то вместо него вывести Foo.
# Если делится на 5 то вывести Bar. Если делится на 3 и на 5 то вывести FooBar.

def task8():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FooBar')
        elif num % 3 == 0:
            print('Foo')
        elif num % 5 == 0:
            print('Bar')
        else:
            print(num)


# task8()

# 9. Hard mode, optional:
# Реализовать фабрику декораторов, инициализируемую с натуральным числом n,
# производящую умножение результата декорируемой
# функции на n если операция применима, иначе возвращающих None.


# Our decorator factory:
def decorator_factory(num):
    # The decorator it creates:
    def decorator(func):
        # The wrapper (what we replace our decorated function with):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res * num

            except TypeError:
                return None

        return wrapper

    return decorator


@decorator_factory(22)
def subtract(a, b):
    return a - b


print(subtract(55, 12))  # >>> 946
