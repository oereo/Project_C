from django.shortcuts import render, HttpResponse
import random, json

import requests
from bs4 import BeautifulSoup as BS

url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'

response = requests.get(url)

if(response.status_code != 200):
    print("%d 에러가 발생하였습니다" % response.status_code)
    quit()

soup = BS(response.content, 'html.parser')
table = soup.find('table', {'class':'table_develop3'})

data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])

# with open('weather.csv') as file:
#     file.write('지역, 기온, 습도 \n')
#     for i in data:
#         file.write('{0}, {1}, {2} \n'.format(i[0], i[1], [2]))
# Create your views here.
def data_json(request):
    
    Fluctuation_ratio = 50  # 등락비율(%)

    ratio = Fluctuation_ratio / float(100)

    init_cost = 31  # 백만원

    Counts = [None, ]

    Costs = ['온도',]

    for i in range(1,31):

        Counts.append(str(i))

        if random.choice((True, False)):

            init_cost += init_cost * ratio

            Costs.append(init_cost)

        else:

            init_cost -= init_cost * ratio

            Costs.append(init_cost)

    data = {

        'columns': [

            Counts,

            Costs,

        ]

    }

    return HttpResponse(json.dumps(data),content_type='text/json')

 

def home(request):
    return render(request,'home.html')


    

# def home(request):
#     template_data = {}
#     time_unit = [i for i in range(1,31)]
#     data1 = np.random.randint(0, high=40, size=30).tolist

#     template_data = {
#         'day': [1,2,3],
#         'temperature': [29,27,33],
#         'time_unit': time_unit,
#         'data1': data1,
        
#     }

#     if request.method == 'GET':
#         print("get...")
#     return render(request, 'home.html', template_data)



#def home(request):
#    return render(request, 'home.html')