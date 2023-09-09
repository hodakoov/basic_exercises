"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from pprint import pprint
from collections import defaultdict

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def find_id_user_most_messages(messages: list) -> int:
    id_users = defaultdict(int)
    for message in messages:
        id_users[message['sent_by']] += 1

    id_user = 0
    max_messages = 0
    for key, value in id_users.items():
        if value > max_messages:
            max_messages = value
            id_user = key

    return id_user


def find_id_user_most_messages_answers(messages: list) -> int:
    id_messages = defaultdict(int)
    for message in messages:
        id_messages[message['reply_for']] += 1

    id_message = 0
    max_answer = 0
    for key, value in id_messages.items():
        if key is None:
            continue
        if value > max_answer:
            max_answer = value
            id_message = key

    for message in messages:
        if message['id'] == id_message:
            return int(message['sent_by'])


def find_id_user_most_see_messages(messages: list) -> list:
    max_count_seen_by = 0
    id_users = []
    for message in messages:
        if len(message['seen_by']) > max_count_seen_by:
            max_count_seen_by = len(message['seen_by'])
            id_users.clear()
            id_users.append(message['sent_by'])
        elif len(message['seen_by']) == max_count_seen_by:
            id_users.append(message['sent_by'])
    unique_id_users = list(set(id_users))
    return unique_id_users


def when_most_messages(messages: list) -> str:
    count_morning = 0
    count_day = 0
    count_evening = 0

    for message in messages:
        time = message['sent_at']
        time = time.time()
        if datetime.time(0, 0, 0) < time < datetime.time(12, 0, 0):
            count_morning += 1
        elif datetime.time(12, 0, 0) <= time <= datetime.time(18, 0, 0):
            count_day += 1
        else:
            count_evening += 1

    if count_morning > count_day and count_morning > count_evening:
        return 'Утром'
    elif count_day > count_evening:
        return 'Днем'
    else:
        return 'Вечером'


# вспомогательная функция для нахождения id сообщения отправителя
def find_id_message(messages: list, id_message) -> str:
    for message in messages:
        if message['id'] == id_message:
            return message['reply_for']


def find_id_messages_which_have_most_threads(messages: list) -> list:
    dict_result = defaultdict(int)
    for message in messages:
        if message['reply_for'] is None:
            continue
        else:
            id_message = message['reply_for']
            count_threads = 0

            while True:
                count_threads += 1
                id_message_find = find_id_message(messages, id_message)
                if id_message_find is None:
                    break
                else:
                    id_message = id_message_find
            dict_result[id_message] = count_threads

    id_message = []
    max_value = 0
    for key, value in dict_result.items():
        if value > max_value:
            max_value = value
            id_message.clear()
            id_message.append(key)
        elif value == max_value:
            id_message.append(key)
    return id_message


if __name__ == "__main__":
    # pprint(generate_chat_history())
    print(find_id_user_most_messages(generate_chat_history()))
    print(find_id_user_most_messages_answers(generate_chat_history()))
    print(find_id_user_most_see_messages(generate_chat_history()))
    print(when_most_messages(generate_chat_history()))
    print(find_id_messages_which_have_most_threads(generate_chat_history()))
