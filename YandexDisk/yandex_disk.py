import requests
from pprint import pprint


class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/'


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


    def _get_upload_link(self):
        url = self.url + 'disk/resources/upload'
        params = {
            'path': 'Fphoto.png',
            'overwrite': 'false'
        }
        headers = self.get_headers()
        req = requests.get(url, headers=headers, params=params)
        if req.status_code == 200:
            print('Ссылка получена')
            return req.json()['href']
        else:
            print(f'Ошибка. \nКод ошибки {req.status_code}')

    def upload(self, file_path: str):
        """ Метод загружает файлы по списку file_list на яндекс диск. """
        url = self._get_upload_link()
        req = requests.put(url, data=open(file_path, 'rb'))
        if req.status_code == 201:
            print('Файл загружен')
        else:
            print(f'Ошибка. \nКод ошибки {req.status_code}')



def get_token(path):
    with open(path) as f:
        token = f.read()
        return token

if __name__ == '__main__':
    token = get_token('token.txt')

    ya = YandexDisk(token)
    ya.upload('Selphi.PNG')

