from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from task.models import Task, TaskState
from utils.messages import ALREADY_EXISTS


class TaskStateSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    class Meta:
        model = TaskState
        exclude = ["task"]

    def get_state(self, obj):
        return TaskState.TaskStateChoices(obj.state).label


class TaskSerializer(serializers.ModelSerializer):
    states = TaskStateSerializer(many=Task, source="taskstate_set", read_only=Task)

    class Meta:
        model = Task
        exclude = []


class TaskStateField(serializers.ChoiceField):
    def __init__(self):
        super(TaskStateField, self).__init__(choices=TaskState.TaskStateChoices.labels)

    def to_internal_value(self, data):
        return TaskState.TaskStateChoices.get_value_by_label(data)

    def to_representation(self, value):
        return TaskState.TaskStateChoices(value).label


class TaskStateAddSerializer(serializers.ModelSerializer):
    state = TaskStateField()

    class Meta:
        model = TaskState
        fields = ["id", "state"]

    def validate_state(self, state):
        if not TaskState.objects.filter(task_id=self.context.get("task_id"), state=state).exists():
            return state
        raise ValidationError(ALREADY_EXISTS)
    
    def create(self, validated_data):
        validated_data["task_id"] = self.context.get("task_id")
        return super(TaskStateAddSerializer, self).create(validated_data)