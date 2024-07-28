def total_salary(path):

    total_salary = 0
    count = 0

    try:
        #Відкриття файлу з with
        #with open(path, 'r', encoding='utf-8') as file:
        for line in path:
            name, salary = line.strip().split(',')
            total_salary += int(salary)
            count += 1
            
    except ValueError:
        print(f"Файл {path} має не коректні дані")
        return None, None
    
    except IndexError:
        print(f"Файл {path} не має даних")
        return None, None

    average_salary = total_salary / count if count > 0 else 0
    return total_salary, average_salary

test_data = [
    "Alex Korp,3000",
    "Nikita Borisenko,2000",
    "Sitarama Raju,1000"
]

total, average = total_salary(test_data)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
