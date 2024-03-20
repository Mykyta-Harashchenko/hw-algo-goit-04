def total_salary(path):
    total_salary = 0
    num_developers = 0
    try:
        with open(path, 'r') as file:  # Using the provided path argument to open the file
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1

        if num_developers == 0:
            return None, None  # Return None if there are no developers

        average = total_salary / num_developers

        return int(total_salary), int(average)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None

    except Exception as e:
        print("Сталася помилка:", e)
        return None, None


checking = total_salary('test.txt')
print(checking)


checking = total_salary('test.txt')
print(checking)