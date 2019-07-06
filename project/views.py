from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def index(request):
	return redirect('signup')

@login_required(login_url='/login')
def base_dashboard(request):
	return render(request, "base_dashboard.html", context={'user': request.user})