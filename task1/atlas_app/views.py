from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'form.html')


def datatables(request):
    return render(request, 'datatables.html')