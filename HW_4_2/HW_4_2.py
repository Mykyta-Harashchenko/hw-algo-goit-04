def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print("Сталася помилка:", e)
        return None

cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    print(cats_info)