import requests



# response = requests.post('http://127.0.0.1:8000/v1/user',
#                          json={'name': 'Name_5',
#                                'email': 'email_5@mail.ru',
#                                'password': 'password'})


# response = requests.post('http://127.0.0.1:8000/v1/adv',
#                          json={'heading': 'Продам автомобиль BMW',
#                                'description': 'Продам Toyota BMW X7, белый ',
#                                'price': '350.50',
#                                'creator': 1})

response = requests.patch('http://127.0.0.1:8000/v1/adv/3',
                         json={
                               'price': '1500000'})

# response = requests.delete('http://127.0.0.1:8000/v1/adv/1')

# response = requests.get('http://127.0.0.1:8000/v1/adv?heading=продам')

# response = requests.get('http://127.0.0.1:8000/v1/adv/2/')


print(response.status_code)
print(response.json())