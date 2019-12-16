from django.http import Http404, request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestSerializers, CollegeUserSerializer,UserProfileSerializer,StudentSerializer
from .models import CollegeUser,UserProfile,Student
import pdb;pdb.set_trace()

class TestView(APIView):
    pdb.set_trace()
    def get(self, request, format=None):
        return Response({"message": "Test View Class GET Method is working."})

    def post(self, request, format=None):
        serializer = TestSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

     # def get(self, request, format=None):
     #     users = CollegeUser.objects.all()
     #     serializer = CollegeUserSerializer(users, many=True)
     #     return Response(serializer.data)

    def get_object(self, pk):
        try:
            pdb.set_trace()
            return CollegeUser.objects.get(pk=pk)
        except CollegeUser.DoesNotExist:
               raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CollegeUserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CollegeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentView(APIView):

      def get_object(self,pk):
          try:
              return Student.objects.get(pk=pk)
          except Student.DoesNotExist:
              raise Http404
      def get(self, request, pk, format=None):
              user=self.get_object(pk)
              serializer=StudentSerializer(user)
              return Response(serializer.data)
      def post(self):
          serializer=StudentSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.status_HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)