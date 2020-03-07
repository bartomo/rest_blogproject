from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry, User
import django_filters
from rest_framework import viewsets, filters
from .serializer import EntrySerializer, UserSerializer
from .forms import EntryForm, SearchForm
import json
import requests

# REST_API用　引数
url = "http://localhost:8000/api/entry/"
headers = {'content-type': 'application/json'}


# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def search(request):
    my_dict ={
        'insert_data': 'ユーザー名検索',
        'form': SearchForm(),
        }
    search_query = request.POST
    if search_query:
        payload = {'user_name': search_query['user_name_query']}
        response = requests.get(url, headers=headers, json=payload)
        result = response.json()
        my_dict['results'] = result
    return render(request, 'search.html', my_dict)


def index(request):
    my_dict = {'form': EntryForm()}
    return render(request, 'index.html', my_dict)


def post_result(request):
    res = requests.post(url, headers=headers, json=request.POST)
    response = res.json()
    result = {
        'insert_data': '投稿結果',
        'result': response}
    return render(request, 'blogposttest.html', result)


def timeline(request):
    try:
        response = requests.get(url, headers=headers)
        result = response.json()
    except Exception:
        pass

    all_data = {
        'insert_data': 'Blog Timeline',
        'all_data': result,
        }
    return render(request, 'blogtimeline.html', all_data)


def base_test(request):
    try:
        response = requests.get(url, headers=headers)
        result = response.json()
    except Exception:
        pass

    all_data = {
        'insert_data': 'Blog Timeline',
        'all_data': result,
        }
    return render(request, 'extends_html_test.html', all_data)

