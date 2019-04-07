import vk
from getpass import getpass

APP_ID = -1


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(
        session,
        v='5.35',
    )
    fields = [
        'first_name',
        'last_name',
        'online'
    ]
    friends = api.friends.get(fields=fields)
    return list(filter(lambda x: x['online'], friends['items']))


def output_friends_to_console(friends_online):
    count_friends = len(friends_online)
    print(
        "Друзья в онлайне {}:".format(count_friends)
    )
    for friend in friends_online:
        first_name = friend['first_name']
        last_name = friend['last_name']
        print(
            "{} {}".format(last_name,first_name)
        )


def main():
    login = input("Введите логин:")
    password = getpass("Введите пароль:")
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        exit()
    output_friends_to_console(friends_online)

if __name__ == '__main__':
    main()
