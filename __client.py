import requests

# BASE_URL = 'http://my-bots.ru:5001'
BASE_URL = 'http://localhost:5001'

# res: dict = requests.post(f'{BASE_URL}/edit/template_bot3/app/handlers/misc.py', json={'text': '333'}).json()
# print(res)
#
# res: dict = requests.post(f'{BASE_URL}/edit/template_bot3/app/handlers/', json={'text': '333'}).json()
# print(res)
#
# res: dict = requests.post(f'{BASE_URL}/edit/template_bot3/app/handlers/misc').json()
# print(res)
#
# res: dict = requests.post(f'{BASE_URL}/edit/template_bot3/app/handlers/misc.py', json={}).json()
# print(res)
#
# res: dict = requests.get(f'{BASE_URL}/get/template_bot3/app/handlers/misc.py').json()
# print(res['text'])

res: dict = requests.get(f'{BASE_URL}/deploy/bot1').json()
print(res)
