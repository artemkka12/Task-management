from rest_framework import serializers

from apps.comments.serializers import CommentSerializer
from apps.tasks.models import Task, Timelog, Timer
from apps.users.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'owner')
        extra_kwargs = {
            'owner': {'read_only': True},
        }


class RetrieveTaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'owner', 'comments')


class AssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('owner', )


class TopTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title')


class TimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timelog
        fields = ('id', 'owner', 'started_at', 'stopped_at', 'duration')


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
            'task': {'read_only': True},
            'is_stopped': {'read_only': True},
            'is_running': {'read_only': True},
            'started_at': {'read_only': True},
            'duration': {'read_only': True},
        }


class ManualTimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timelog
        fields = '__all__'
        extra_kwargs = {
            'task': {'read_only': True},
            'stopped_at': {'read_only': True},
            'owner': {'read_only': True},
        }
