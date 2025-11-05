from .serializers import UserSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import TaskModel
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print("Received data:", request.data)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=400)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
# request.data is where the credentials sent from a POST request is stored. so we are attributing that data to the serializer data. the serializer variable is an instance 
    
class TaskView(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        currentUser = self.request.user
        return TaskModel.objects.filter(taskOwner=currentUser)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(taskOwner=self.request.user)
        else:
            print(serializer.errors)

class DeleteTask(generics.DestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner = self.request.user
        return TaskModel.objects.filter(taskOwner=owner)

    
class ToggleComplete(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        item = get_object_or_404(TaskModel, pk=pk)
        item.status = not item.status
        item.save(update_fields=["status"])
        return Response({"id": item.id, "status": item.status})
    
    # clarificatiion on this code

