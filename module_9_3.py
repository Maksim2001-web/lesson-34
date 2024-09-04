first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(s1) - len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))
print(list(first_result))  # [1, 2]

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))  # [False, False, True]
