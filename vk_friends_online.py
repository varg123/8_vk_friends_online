import vk
from getpass import getpass
import requests

APP_ID = -1
VK_API_VERSION = '5.92'


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(
        session,
        v=VK_API_VERSION
    )
    fields = [
        'first_name',
        'last_name',
        'online'
    ]
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids, fields=fields)


def output_friends_to_console(friends_online):
    count_friends = len(friends_online)
    print(
        "Друзья в онлайне {}:".format(count_friends)
    )
    for friend in friends_online:
        first_name = friend['first_name']
        last_name = friend['last_name']
        print(
            "{} {}".format(last_name, first_name)
        )


def main():
    login = input("Введите логин:")
    password = getpass("Введите пароль:")
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        exit("Неверный логин или пароль")
    except requests.exceptions.ConnectionError:
        exit("Ошибка соединения")
    output_friends_to_console(friends_online)

if __name__ == '__main__':
    main()
