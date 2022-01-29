from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
klass_list = ((el_1, el_2) for el_1, el_2 in zip_longest(tutors, klasses))

print(list(klass_list))
