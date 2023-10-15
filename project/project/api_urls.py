from django.urls import path, include

urlpatterns = [
    path('user/', include('user_auth.urls'))
]