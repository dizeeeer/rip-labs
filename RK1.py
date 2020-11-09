from operator import itemgetter


class hom:
    """ДОм"""

    def __init__(self, id, name, capacity, price, comp_id):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.price = price
        self.comp_id = comp_id


class Str:
    """Улица"""

    def __init__(self, id, model):
        self.id = id
        self.model = model


class Strhom:
    """
    'Дома на улицах' для реализации
    связи многие-ко-многим
    """

    def __init__(self, comp_id, hom_id):
        self.comp_id = comp_id
        self.hom_id = hom_id


# Улицы
Streets = [
    Str(1, 'Плещеева'),
    Str(2, 'Аркадная'),
    Str(3, 'Арочная'),

    Str(11, 'Фестивальная'),
    Str(22, 'Ягодная'),
    Str(33, 'zzzzпв'),
]

# Дома
homs = [
    hom(1, 'А', '14', 1795000, 1),
    hom(2, 'АА', '2', 3259000, 2),
    hom(3, 'ААА', '33', 6155500, 22),

    hom(4, 'АААА', '23', 3290780, 3),
    hom(5, 'ААААА', '2', 234500, 11),
    hom(6, 'АААААА', '56', 176430, 33),
]

Strs_homs = [
    Strhom(1, 1),
    Strhom(2, 2),
    Strhom(3, 3),
    Strhom(3, 4),
    Strhom(3, 5),

    Strhom(11, 1),
    Strhom(22, 2),
    Strhom(33, 3),
    Strhom(33, 4),
    Strhom(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(h.name, h.capacity, h.price, c.model)
                   for c in Streets
                   for h in homs
                   if h.comp_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.model, ch.comp_id, ch.hom_id)
                         for c in Streets
                         for ch in Strs_homs
                         if c.id == ch.comp_id]

    many_to_many = [(h.name, h.capacity, h.price, comp_model)
                    for comp_model, comp_id, hom_id in many_to_many_temp
                    for h in homs if h.id == hom_id]

    print('Задание Г1')
    res_11 = list(filter(lambda x: x[3].startswith('А'), one_to_many))
    print(res_11)

    print('\nЗадание Г2')
    res_12_unsorted = []
    # Перебираем все улицы
    for c in Streets:
        # Список домов
        c_homs = list(filter(lambda i: i[3] == c.model, one_to_many))
        # Если есть улица
        if len(c_homs) > 0:
            # Стоимость дома
            c_prices = [price for _, _, price, _ in c_homs]
            # Максимальная стоимость дома
            c_prices_max = max(c_prices)
            res_12_unsorted.append((c.model, c_prices_max))

    # Сортировка по max стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    for i in res_12:
        print(i)


    print('\nЗадание Г3')
    res_13 = sorted(many_to_many, key=itemgetter(3))
    for i in res_13:
        print(i)


if __name__ == '__main__':
    main()
