import requests
import json


def requests_super_heroes(url):
    resp = requests.get(url)
    return resp.json()


def write_super_heroes(data):
    ''' Create JSON file with super_heroes. '''
    with open('super_heroes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def sorted_heroes(arr, powerstat="intelligence", *heroes):
    heroes_ = {}
    for hero in arr:
        if hero['name'] in heroes:
            heroes_[hero['name']] = hero['powerstats'][powerstat]
    sorted_heroes = sorted(
        heroes_.items(), key=lambda item: item[1], reverse=True)
    return sorted_heroes


if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    super_heroes = requests_super_heroes(url)
    # write_super_heroes(super_heroes)
    heroes = sorted_heroes(super_heroes, "intelligence",
                           'Hulk', 'Captain America', 'Thanos')
    print('Самый топовый герой: ' +
          ', затем '.join(str(x[0]) + ' (показатель: ' + str(x[1]) + ')' for x in heroes))
