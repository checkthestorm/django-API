from django.contrib import admin
from django.urls import path, include
from .views import UserView, TaskView, ToggleComplete, DeleteTask
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/register/', UserView.as_view(), name='user-register'),
    path('api/tasks/', TaskView.as_view()),
    path('api/<int:pk>/status/', ToggleComplete.as_view()),
    path('api/tasks/<int:pk>/', DeleteTask.as_view()),

    # learn the concept of token/authentications
    path('api-auth/', include('rest_framework.urls'), name='rest_frameworkk'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
