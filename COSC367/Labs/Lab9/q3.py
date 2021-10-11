import csv

def learn_prior(file_name, pseudo_count=0):
    count = index = 0
    skip_head = 1
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        file = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i in file:
            if skip_head:
                skip_head = 0
                continue
            index += 1
            if i[-1] == '1':
                count += 1
    result = count + pseudo_count / (index + 2 * pseudo_count)
    return result
