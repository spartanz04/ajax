from django.shortcuts import render, redirect
from .form import ApplicationForm



# Create your views here.
def home(request):
    return render(request,"ajax/index.html")

def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def courses(request):
    return render(request,"courses.html")
def contact(request):
    return render(request,"contact.html")

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    
    return render(request, 'apply.html', {'form': form})

def success(request):
    return render(request, 'success.html')  # Render the success page



