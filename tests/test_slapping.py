import requests
from slapping.slap_that_like_button import mintemp, mediumtemp, maxtemp
# from slapping.slap_that_like_button import LikeState, slap_many

checkData = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
checkTemperatures = []

for i in checkData.json()['data']:
    temp = i['temperature']
    checkTemperatures.append(temp)

checkTemperatures.sort()

def test_min():
    assert mintemp() == checkTemperatures[0]


def test_medium():
    assert mediumtemp() == checkTemperatures[2]


def test_():
    assert maxtemp() == checkTemperatures[4]