import csv


def get_list_from_file(path):
    with open(f"north_data/{path}", "r", encoding="utf-8") as f:
        file_list = csv.reader(f)
        total = []
        for el in file_list:
            total.append(el)

    return total



