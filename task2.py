def get_cats_info(path: str):
    cats_info_dictionary = []

    try:
        with open(path, "r") as fh:
            lines = [el.strip() for el in fh.readlines()]
            for line in lines:
                cat_id, cat_name, cat_age = line.split(',')
                cats_info_dictionary.append({
                    'id': cat_id,
                    'name': cat_name,
                    'age': cat_age
                })

            return cats_info
    except (FileNotFoundError, IOError):
        print('Wrong file or file path')


cats_info = get_cats_info('./casts_file.txt')
print(cats_info)
