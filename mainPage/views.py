from django.shortcuts import render, HttpResponse
import random, json

from urllib.request import urlopen, Request
import urllib
import bs4

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


location = '장기동'
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')
print('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')


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