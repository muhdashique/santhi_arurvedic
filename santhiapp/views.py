from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')




def about(request):
    return render(request,'about.html')
    



def facilities(request):
    return render(request,'facilities.html')    



def gallery(request):
    return render(request,'gallery.html')      





def treatment(request):
    return render(request,'treatment.html')




def advtreatment(request):
    return render(request,'advtreatment.html')





