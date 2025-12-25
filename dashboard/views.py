from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser
from events.models import Event
from alerts.models import Alert
from django.db.models import Count
from accounts.utils import log_user_activity
import json

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            log_user_activity(user, 'login', 'accounts', f"User {username} logged in successfully.", request)
            return redirect('dashboard_home')
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'dashboard/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'analyst')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role)
            login(request, user)
            log_user_activity(user, 'user_registered', 'accounts', f"New user {username} registered as {role}.", request)
            return redirect('dashboard_home')
            
    return render(request, 'dashboard/register.html')

def logout_view(request):
    if request.user.is_authenticated:
        log_user_activity(request.user, 'logout', 'accounts', f"User {request.user.username} logged out.", request)
    logout(request)
    return redirect('login')

@login_required
def dashboard_home(request):
    total_events = Event.objects.count()
    total_alerts = Alert.objects.count()
    open_alerts = Alert.objects.filter(status='open').count()
    
    recent_events = Event.objects.all().order_by('-timestamp')[:10]
    
    severity_stats = list(Event.objects.values('severity').annotate(count=Count('id')))
    for stat in severity_stats:
        stat['percentage'] = (stat['count'] / total_events * 100) if total_events > 0 else 0
    
    context = {
        'total_events': total_events,
        'total_alerts': total_alerts,
        'open_alerts': open_alerts,
        'recent_events': recent_events,
        'severity_stats': severity_stats,
    }
    return render(request, 'dashboard/index.html', context)

from django.core.paginator import Paginator

@login_required
def event_list(request):
    event_list = Event.objects.all().order_by('-timestamp')
    paginator = Paginator(event_list, 20)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)
    return render(request, 'dashboard/events.html', {'events': events})

@login_required
def alert_list(request):
    alert_list = Alert.objects.all().order_by('-created_at')
    paginator = Paginator(alert_list, 20)
    page_number = request.GET.get('page')
    alerts = paginator.get_page(page_number)
    return render(request, 'dashboard/alerts.html', {'alerts': alerts})

from accounts.models import CustomUser, UserActivity

@login_required
def activity_log(request):
    activity_list = UserActivity.objects.all().order_by('-timestamp')
    paginator = Paginator(activity_list, 20)
    page_number = request.GET.get('page')
    activities = paginator.get_page(page_number)
    return render(request, 'dashboard/activity.html', {'activities': activities})

from django.http import JsonResponse

@login_required
def alert_stats_json(request):
    count = Alert.objects.filter(status='open').count()
    return JsonResponse({'unresolved_count': count})


@login_required
def alert_status_change(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            alert_id = data.get('alert_id')
            new_status = data.get('new_status')
            notes = data.get('resolution_notes')
            
            alert = Alert.objects.get(id=alert_id)
            old_status = alert.status
            alert.status = new_status
            if notes is not None:
                alert.resolution_notes = notes
            alert.assigned_to = request.user
            alert.save()

            action = 'alert_resolved' if new_status == 'resolved' else 'alert_acknowledged'
            log_user_activity(
                request.user, 
                action, 
                'alerts', 
                f"Changed Alert #{alert_id} status from {old_status} to {new_status}.",
                request
            )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid method'})