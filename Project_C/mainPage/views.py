from django.shortcuts import render, HttpResponse
import random
import json
import requests
from bs4 import BeautifulSoup as BS

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer

@api_view(["GET"])
def HelloAPI(request):
    return Response("hello world!")


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


def data_json(request):

    Fluctuation_ratio = 50  # 등락비율(%)

    ratio = Fluctuation_ratio / float(100)

    init_cost = 31  # 백만원

    Counts = [None, ]

    Costs = ['온도', ]

    for i in range(1, 31):

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

    return HttpResponse(json.dumps(data), content_type='text/json')


def home(request):
    url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
    response = requests.get(url)
    if(response.status_code != 200):
        print("%d 에러가 발생하였습니다" % response.status_code)
        quit()

    soup = BS(response.content, 'html.parser')
    table = soup.find('table', {'class': 'table_develop3'})

    data_temp = []
    for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))
        for td in tds:
            if td.find('a'):
                point = td.find('a').text
                temperature = tds[5].text
                humidity = tds[9].text
                data_temp.append([point, temperature, humidity])
    return render(request, "home.html", {'data_temp':data_temp})


