def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            for number in numbers:
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
            return 0

        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_data
        if valid_count == 0:
            return 0

        return total_sum / valid_count

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
