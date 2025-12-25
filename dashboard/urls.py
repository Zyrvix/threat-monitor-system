from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.event_list, name='event_list'),
    path('alerts/', views.alert_list, name='alert_list'),
    path('activity/', views.activity_log, name='activity_log'),
    path('api/stats/', views.alert_stats_json, name='alert_stats_json'),
    path('alert_status_change/', views.alert_status_change, name='alert_status_change'),
]
