import csv

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

result = set()
with open('output/csv/street.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if not (row):    
            continue
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\tWord: {row[0]} - Value: {row[1]}.')
            line_count += 1
            unique_row_items = set(field.strip().lower() for field in row)
            for item in unique_row_items:
                if is_number(item) == False:
                    result.add(item)

print(result)
