from Common.Utils.regex import (
    get_short_url,
    remove_space,
)
from Common.Utils.storage import (
    dump_data,
    load_data,
    get_key,
    get_homepage_name,
    get_short_and_url,
    get_alias_and_homepage_all,
    get_short_and_url_all,
    get_alias_from_db,
)
from Common.Utils.url_request import get_response, get_status
from Common.messages import (
    MES_SHORT_URL,
    MES_ALIAS,
    MES_STANDART_URL,
    MES_HOME_URL,
    MES_STATUS,
    MES_PROGRAM_NAME,
    MES_BEGIN,
    MES_CHOICE,
    MES_INPUT,
    MES_INPUT_URL,
)


if __name__ == '__main__':
    print(MES_PROGRAM_NAME)
    while True:
        print('\n', MES_BEGIN)
        choice = input(MES_CHOICE)

        if choice == '1':
            url = input(MES_INPUT_URL)
            data = get_short_url(url)

            if isinstance(data, dict):
                alias = get_key(data)

                database = load_data(0)
                database[alias] = data[alias]
                dump_data(database, 0)

                print(MES_SHORT_URL, data[alias]['short_url'])
                print(MES_ALIAS, alias)
                print(MES_STANDART_URL, data[alias]['url'])
            else:
                print(data)

        elif choice == '2':
            alias = input(MES_INPUT + MES_ALIAS.lower())
            alias = remove_space(alias)

            database = load_data(0)
            homepage: str = get_homepage_name(database, alias)

            print(MES_HOME_URL, homepage)
            print(MES_ALIAS, get_alias_from_db(database, alias))

            response = get_response(homepage)

            print(MES_STATUS, get_status(response))

        elif choice == '3':
            short_url = input(MES_INPUT + MES_SHORT_URL.lower())
            short_url = remove_space(short_url)
            data = load_data(0)

            url, short = get_short_and_url(data, short_url)

            print(MES_STANDART_URL, url)
            print(MES_SHORT_URL, short)

            response = get_response(url)

            print(MES_STATUS, response)

        elif choice == '4':
            data = load_data(0)
            print(MES_ALIAS)
            print(get_alias_and_homepage_all(data))

            print(MES_SHORT_URL)
            print(get_short_and_url_all(data))

        elif choice == '5':
            break
