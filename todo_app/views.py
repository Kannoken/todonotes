from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo_app.serializers import TodoSerializer
from todo_app.models import Todo


class TodoView(APIView):
    def get(self, request):
        """
        get all created todo-notes
        """
        all_to_noted = Todo.objects.all()
        serializer = TodoSerializer(all_to_noted, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        add new todo-note
        """
        serializer = TodoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        todo_obj = Todo(description=data['description'], is_done=False)
        todo_obj.save()
        request.data['id'] = todo_obj.id
        return Response(request.data, status=status.HTTP_201_CREATED)

    def delete(self, request, todo_id):
        """
        delete todo note
        """
        Todo.objects.get(id=todo_id).delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, todo_id):
        """
        update already saved todo note
        """
        serializer = TodoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        desc = data['description']
        is_done = data['is_done']
        todo_obj = Todo(id=todo_id, description=desc, is_done=is_done, updated=datetime.now())
        todo_obj.save()
        return Response(status=status.HTTP_200_OK)

