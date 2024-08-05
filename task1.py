def total_salary(path: str):
    total_salary_value = 0

    try:
        with open(path, "r") as fh:
            lines = [el.strip() for el in fh.readlines()]
            for line in lines:
                name, salary = line.split(',')
                total_salary_value += int(salary)

            return total_salary_value, total_salary_value / len(lines)
    except (FileNotFoundError, IOError):
        print('Wrong file or file path')


try:
    total, average = total_salary('./salary_fisle.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print('Can\'t get the values')