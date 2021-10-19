from telethon import functions, types, errors
from telethon.sync import TelegramClient
import config
import asyncio
import random


api_id = config.api_id
api_hash = config.api_hash
loop = asyncio.get_event_loop()


def print_user(full_user):
    """
    Функция для вывода информации об импортируемом номере
    """

    full_user = full_user.user
    # Разбиваем основную инфу по переменным
    user_id = full_user.id
    name = full_user.first_name
    if full_user.last_name is not None:
        name = f"{name} {full_user.last_name}"
    if full_user.username is not None:
        username = full_user.username
    else:
        username = "-"
    phone = full_user.phone
    print(
        f"ID пользователя: {user_id}\n"
        f"Имя пользователя: {name}\n"
        f"Username: {username}\n"
        f"Номер телефона: {phone}\n"
    )


async def main():
    number = input("Номер телефона: ")
    async with TelegramClient(f"session", api_id, api_hash) as client:
        try:
            # Добавляем контакт
            result = await client(
                functions.contacts.ImportContactsRequest(
                    contacts=[
                        types.InputPhoneContact(
                            client_id=random.randrange(-(2 ** 63), 2 ** 63),
                            first_name=number,
                            last_name="",
                            phone=number,
                        )
                    ]
                )
            )
            # Если импорт успешен
            if len(result.imported) > 0:
                user = result.users[0]
                # Если в конфиге параметр send_user = True, то контакт отправляется в раздел "Избранное"
                if config.send_user:
                    await client.send_file(
                        "me",
                        types.InputMediaContact(
                            phone_number=number,
                            first_name=number,
                            last_name="",
                            vcard="",
                        ),
                    )
                # Получаем информацию о контакте
                result = await client(functions.contacts.GetContactsRequest(hash=0))
                # Удаление контакта
                await client(functions.contacts.DeleteContactsRequest(id=result.users))
                # Получаем информацию о только что удалённом контакте.
                full_user = await client(functions.users.GetFullUserRequest(id=user))
                # Контакт получен, основная часть закончена

                # По желанию, выводим инфу о юзере на экран
                print_user(full_user)
            else:
                #  Если импорт без результата:
                print("Упс... Такого контакта в TG не обнаружено.")
        except errors.FloodWaitError as e:
            print(f"Вы получили ограничение на испольование API на {e.seconds} секунд")


loop.run_until_complete(main())
