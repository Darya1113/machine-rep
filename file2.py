# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, sym = ','):
    list1 = str1.split(sym)
    list2 = str2.split(sym)
    list_out = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list_out.append(list1[i])
    return list_out

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))