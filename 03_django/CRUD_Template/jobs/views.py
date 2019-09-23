import requests
from django.shortcuts import render, redirect
from .models import Job
from decouple import config
from faker import Faker
# Create your views here.


def index(request):
    return render(request, 'jobs/index.html')


def past_life(request):
    # 사용자로부터 이름 데이터 받기
    name = request.POST.get('name')

    # db 에 매칭 되는 name 가져오기
    # Job.objects.get()
    # get 이 더 간단하지만 값이 없으면 에러 발생
    # filter 사용
    person = Job.objects.filter(name=name).first()

    # DB 에 person 이 있는지 없는지 확인
    if person:
        past_job = person.past_job
    else:  # db 에 기존 이름이 없다면 (person  이 빈 쿼리셋 == False)
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job)  # 새로운 레코드를 추가한다.
        person.save()

    # GIPHY (past_job 을 API 에 요청을 보내서 응답을 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')

    context = {'person': person, 'image': image, }
    return render(request, 'jobs/past_life.html', context)
