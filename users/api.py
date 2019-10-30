from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserSerialzier


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzier


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzier
