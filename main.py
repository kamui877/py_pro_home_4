from itertools import chain

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
nested_list2 = [['a', 'b', ['c', [2, 3]]], ['d', ['e', 'f'], 'h', False], [1, 2, None]]


# Класс с известным уровнем вложенности
class ListIter(list):
    def __iter__(self):
        result = []
        for val in range(len(self)):
            result.extend(self[val])
        return chain(result)


flat_list = [item for item in ListIter(nested_list)]
print(flat_list, 'Класс с известным уровнем вложенности')


# Генератор с известным уровнем вложенности
def list_iter(list_):
    result = []
    for val in range(len(list_)):
        result.extend(list_[val])
    for el in result:
        yield el


flat_list2 = [item for item in list_iter(nested_list)]
print(flat_list2, 'Генератор с известным уровнем вложенности')


# Функция для любого уровня вложенности
def join_list(list_):
    result = []
    for el in list_:
        if isinstance(el, list):
            result.extend(join_list(el))
        else:
            result.append(el)
    return result


# Класс с любым уровнем вложенности
class ListIterHard(list):
    def __iter__(self):
        return chain(join_list(self))


#flat_list3 = [item for item in ListIterHard(nested_list2)]
#print(flat_list3, 'Класс с любым уровнем вложенности')
#Почему то когда я запукаю этот класс, выдает ошибку рекурсии. Не понимаю как это исправить.

# Генератор с любым уровнем вложенности
def list_iter_hard(list_):
    for el in join_list(list_):
        yield el


flat_list4 = [item for item in list_iter_hard(nested_list2)]
print(flat_list4, 'Генератор с любым уровнем вложенности')


