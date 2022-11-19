from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'first_name':'firstName:Manju',
        'last_name':'lastName:Latha',
        'email':'mailID:manju@gmail.com',
        'phone':'PH:1234565234'
        }
    return render(request,'manju.html',context)