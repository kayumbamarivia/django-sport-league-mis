from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Schedule
from .forms import ScheduleForm

@login_required(login_url="/login/")
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})

@login_required(login_url="/login/")
def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'schedules/schedule_detail.html', {'schedule': schedule})

@login_required(login_url="/login/")
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule created successfully!")
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/schedule_form.html', {'form': form})

@login_required(login_url="/login/")
def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule updated successfully!")
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedules/schedule_form.html', {'form': form})

@login_required(login_url="/login/")
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, "Schedule deleted successfully!")
        return redirect('schedule_list')
    return render(request, 'schedules/schedule_confirm_delete.html', {'schedule': schedule})
