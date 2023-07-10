from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from task.models import Task
from task.serializers import TaskSerializer, TaskStateAddSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.prefetch_related("taskstate_set").all()

    @action(detail=Task, methods=["put"], name="add_state")
    def add_state(self, request, pk):
        serializer_obj = TaskStateAddSerializer(data=request.data, context={"task_id": pk})
        serializer_obj.is_valid(raise_exception=Task)
        serializer_obj.save()
        return Response(data=serializer_obj.data, status=status.HTTP_201_CREATED)
