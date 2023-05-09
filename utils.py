import datetime
import json
from operator import itemgetter


def load_json(data):
    """
    Десериализация JSON-файла
    :param data: json-файл
    :return: Файл для работы в python
    """
    with open(data, "r", encoding="utf-8") as file:
        json_file = json.load(file)
        return json_file


def time_sorted_data(data):
    """
    Сортировка данных в файле по полю времени
    :param data: Файл с данными
    :return: Отсортированный файл с данными
    """
    data = sorted(data, key=itemgetter('date'), reverse=True)

    for string in data:
        string["date"] = ".".join(string["date"][:10].split("-")[::-1])

    return data


def state_sorted_data(data, value):
    """
    Функция оставляет строки с нужным значением
    :param data: Список словарей
    :param value: Значение, по которому осуществлять поиск в ключе state
    :return: Отсортированный по значению список словарей
    """
    key_list = []

    for string in data:
        if string["state"] == value:
            key_list.append(string)
    return key_list


def card_with_code(card):
    """
    Функция для шифрования номера карты отправителя в формате XXXX XX** **** XXXX
    :param card: Номер карты
    :return: Зашифрованный номер карты в формате
    """
    split_card = card.split(" ")
    card = split_card[-1]
    part_card = " ".join([card[:4], card[4:6]])
    card = "-".join([part_card, card[-4:]])

    if len(split_card) == 3:
        return " ".join([split_card[len(split_card) - 3], split_card[len(split_card) - 2],
                         card.replace("-", "** **** **** ")])
    elif len(split_card) == 2:
        return " ".join(
            [split_card[len(split_card) - 2], card.replace("-", "** **** **** ")])
    else:
        return card.replace("-", "** **** **** ")


def account_with_code(account):
    """
    Функция для шифрования номера счета получателя в формате **XXXX
    :param account: Номер счета
    :return: Зашифрованный номер карты в формате
    """
    split_account = account.split(" ")
    account = split_account[-1]
    account = "**** **** **** **** " + account[-4:]

    if len(split_account) == 3:
        return " ".join(
            [split_account[len(split_account) - 3], split_account[len(split_account) - 2],
             account])
    elif len(split_account) == 2:
        return " ".join([split_account[len(split_account) - 2], account])
    else:
        return account


def output(data):
    """
    Функция для формирования вывода последних 5 операций клиента в соответствующем формате
    :param data: json-файл
    :return: данные для вывода последних 5 операций клиента в соответствующем формате
    """
    output_data = []
    data = load_json(data)
    # Сортировка элементов списка по дате
    sorted_data = time_sorted_data(data)
    # Сортировка элементов списка по статусу
    result_data = state_sorted_data(sorted_data, "EXECUTED")

    for string in result_data:
        data = {
            "date": string["date"],
            "description": string["description"],
            # "from": card_with_code(string["from"]),
            "to": account_with_code(string["to"]),
            "amount": string["operationAmount"]["amount"],
            "name": string["operationAmount"]["currency"]["name"]
        }
        output_data.append(data)

    return output_data[:5]


print(output("operations.json"))

