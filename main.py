import requests
import json

data = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
temperatures = []

def mintemp():
    return temperatures[0]

def mediumtemp():
    return temperatures[2]

def maxtemp():
    return temperatures[4]


for i in data.json()['data']:
    temp = i['temperature']
    temperatures.append(temp)
    
temperatures.sort()

def main():
    checkData = requests.post('https://tues2022.proxy.beeceptor.com/my/api/test')
    checkTemperatures = []
    
    for i in data.json()['data']:
        temp = i['temperature']
        checkTemperatures.append(temp)

    checkTemperatures.sort()

    assert mintemp() == checkTemperatures[0]
    assert mediumtemp() == checkTemperatures[2]
    assert maxtemp() == checkTemperatures[4]


if __name__ == '__main__':
    main()