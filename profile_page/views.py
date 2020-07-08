from django.shortcuts import render

# Create your views here.
def profile_view(request):
    val=5
    return render(request,"profile_page/profile.html",{'val':val})