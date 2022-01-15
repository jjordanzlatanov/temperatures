import requests
from main import mintemp, mediumtemp, maxtemp

data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
temperatures = []


for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)


temperatures.sort()


def test_mintemp():
    assert mintemp() == temperatures[0]


def test_mediumtemp():
    assert mediumtemp() == temperatures[2]


def test_maxtemp():
    assert maxtemp() == temperatures[4]
