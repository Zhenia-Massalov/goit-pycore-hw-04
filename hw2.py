def get_cats_info(data):

    cats_data = []
    try:
        #Відкриття файлу з with
        #with open(path, 'r', encoding='utf-8') as file:
        for line in data:
            cat_id, cat_name, cat_age = line.strip().split(',')
            cat_info = {
                "id": cat_id,
                "name": cat_name,
                "age": int(cat_age)
            }
            cats_data.append(cat_info)
            
    except FileNotFoundError:
        print(f"Файл {data} не знайдено.")
        
    except ValueError:
        print("Некоректний формат даних в файлі.")
    return cats_data

test_data = [
"60b90c1c13067a15887e1ae1,Tayson,3",
"60b90c2413067a15887e1ae2,Vika,1",
"60b90c2e13067a15887e1ae3,Barsik,2",
"60b90c3b13067a15887e1ae4,Simon,12",
"60b90c4613067a15887e1ae5,Tessi,5",
]

cats_info = get_cats_info(test_data)
print(cats_info)
