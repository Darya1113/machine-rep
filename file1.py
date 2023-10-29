# TODO Напишите функцию для поиска индекса товара

def in_list(spisok, tovar):
    flag = False
    for i in range(len(spisok)):
        if spisok[i] == tovar:
            flag = True
            return i
    if not flag:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = in_list(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
