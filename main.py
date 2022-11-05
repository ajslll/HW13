#1
'''def change(lst):
    if len(lst) < 2:
        print('Error')
        exit()
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change(['Candle', 'shop', 123, 'Mac', 12]))'''

#2
'''def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([123,'Mac', 'Candle', (321, 12)]))'''

#3
'''def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))
print(sum_range(1, 5))'''

#4

def read_last(lines, file):
    if lines < 1 or type(lines) != int:
        print('Только положительное число')
    else:
        with open(file, encoding='utf-8') as k:
            file_lines = k.readlines()[-lines:]
        for j in file_lines:
            print(j.strip())

read_last(3, 'file.txt')
