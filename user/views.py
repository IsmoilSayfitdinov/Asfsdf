from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserModelsSerializers


class User(APIView):
    def get(self, requets):
        users = UserModel.objects.all()
        serializer = UserModelsSerializers(users, many=True)
        
        if users.count() == 0:
            res = {
                "success":False,
                "status": status.HTTP_204_NO_CONTENT,
                "data":[]
            }
        else:
            res = {
                "success":True,
                "status":status.HTTP_200_OK,
                "data":serializer.data
            }
        
        return Response(res)
    
    
class UserDetail(APIView):
    def get(self, request, pk):
        book_detail_for_pk_get = UserModel.objects.filter(pk=pk).first()
        serializer = UserModelsSerializers(book_detail_for_pk_get)
        
        if book_detail_for_pk_get:
            res = {
            "success":True,
            "status":status.HTTP_200_OK,
            "data":serializer.data
            }
        else:
            res = {
                "success":False,
                "status":status.HTTP_404_NOT_FOUND,
            }
        
        return Response(res)
    


class UserCreate(APIView):
    def post(self, request):
        serializer = UserModelsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'User is created',
                'book': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class UserUpdate(APIView):
    def put(self, request, pk):
        user = UserModel.objects.filter(pk=pk).first()
        serializer = UserModelsSerializers(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'User is updated',
                'book': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class UserDelate(APIView):
    def delete(self, request, pk):
        user = UserModel.objects.filter(pk=pk).first()
        if user:
            user.delete()
            response = {
                'success': True,
                'message': 'User is deleted',
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)