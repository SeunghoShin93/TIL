from rest_framework.response import Response
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Todo
from django.contrib.auth import get_user_model
#from rest_framework.authentication import JSONWebTokenAuthentication
# Create your views here.

User = get_user_model()


@api_view(['POST'])
# settings.py 에 default 로 설정했기때문에 아래 두 데코레이터는 설정하지 않아도 된다.
# 1. 인증 받은 사용자만 허가 (로그인 여부만 체크)
# @permission_classes((IsAuthenticated, ))
# 2. jwt 인증
# @authentication_classes((JSONWebTokenAuthentication, ))
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204: 해당하는 컨텐츠가 없는 경우 (삭제했기 떄문에 해당 데이터 존재 x)
        return Response(status=204)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입 성공'})


@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)
