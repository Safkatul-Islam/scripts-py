def _calc_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def add_student(records, name, grades):
    records[name] = grades


def get_average(records, name):
    if name not in records:
        return None
    return _calc_average(records[name])


def get_top_student(records):
    if not records:
        return None
    return max(records, key=lambda name: _calc_average(records[name]))


def list_students(records):
    sorted_students = sorted(records.items(), key=lambda item: _calc_average(item[1]), reverse=True)
    for name, grades in sorted_students:
        print(f'{name}: {_calc_average(grades):.2f}')


# Test it
records = {}
add_student(records, "Alice", [88, 92, 79])
add_student(records, "Bob", [70, 68, 84])
add_student(records, "Carol", [95, 98, 100])

print(get_average(records, "Alice"))   # 86.33
print(get_top_student(records))        # Carol
list_students(records)
# Carol: 97.67
# Alice: 86.33
# Bob: 74.0