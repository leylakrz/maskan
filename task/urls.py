from rest_framework.routers import DefaultRouter

from task.views import TaskViewSet

task_router = DefaultRouter()
task_router.register('', TaskViewSet, basename='task')
urlpatterns = [

              ] + task_router.urls
