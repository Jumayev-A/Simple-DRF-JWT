from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user import serializers
from django.contrib.auth.models import User
from user.models import UserModel
from user.serializers import UserModelSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


@csrf_exempt
@api_view(['POST'])
def user_register(request, format=None):
    if request.method == 'POST':
        username = request.data['username']
        phone = request.data['phone']
        password = request.data['password']
        amount = request.data['amount']
        is_admin = request.data['is_admin']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User is already exists'}, safe=False, status=409)
        if is_admin in ['True', 'true', 'False', 'false']:
            if is_admin in ['True', 'true']:
                user = User.objects.create_user(username=username, password=password, is_superuser=True)
                UserModel.objects.create(user=user, phone=phone, amount=amount)
            else:
                user = User.objects.create_user(username=username, password=password, is_superuser=False)
                UserModel.objects.create(user=user, phone=phone, amount=amount)
        else:
            return JsonResponse({'error': 'is_admin field is undefined'}, safe=False, status=400)
        return JsonResponse({'success': 'User successfully registered'}, safe=False, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request, format=None):
    if request.method == 'GET':
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)






    