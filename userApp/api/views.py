from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from userApp.api.serializer import SerializerUser


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def login_view(request):
    data = {}

    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        account = auth.authenticate(email=email, password=password)

        if account is not None:  # Diferente de vacio
            data['response'] = 'Login exitoso'
            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "wrong credentials"
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = SerializerUser(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors

        return Response(data)
