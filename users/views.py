from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .models import User
from .serializers import (
    UserBalanceAddSerializer,
    UserBalanceSubstractSerializer,
    UserBalanceSendSerializer,
    UserBalanceCheckSerializer,
)


class UserBalanceAdd(APIView):
    def put(self, request):
        serializer = UserBalanceAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response(
                {'status': status.HTTP_404_NOT_FOUND, 'error': {'message': 'data are not valid'}}
            )


class UserBalanceSubtract(APIView):
    def put(self, request):
        serializer = UserBalanceSubstractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response(
                {'status': status.HTTP_404_NOT_FOUND, 'error': {'message': 'data are not valid'}}
            )


class UserBalanceSend(APIView):
    def put(self, request):
        serializer = UserBalanceSendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response(
                {'status': status.HTTP_404_NOT_FOUND, 'error': serializer.errors}
            )


class UserBalanceCheck(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBalanceCheckSerializer