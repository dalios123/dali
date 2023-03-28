from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserAccountSerializer

from .forms import SignupForm

from .models import UserAccount


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['DateDeNaissance'] = user.DateDeNaissance.strftime("%Y-%m-%d")
        token['is_expert'] = user.is_expert
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['POST'])
def Signup(request):
    form = SignupForm(request.data)
    print(request.data['DateDeNaissance'])
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        DateDeNaissance = form.cleaned_data.get('DateDeNaissance')
        user = UserAccount.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, password=password, DateDeNaissance=DateDeNaissance)
        return Response(UserAccountSerializer(user).data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
