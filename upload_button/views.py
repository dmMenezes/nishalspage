from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import user_content
from .models import UploadedContent
import imghdr



def button_upload(request):
    form=user_content()
    if(request.method=="POST" and 'save_to_db' in request.POST):
        user=request.POST['user']
        caption=request.POST['caption']
        img=request.POST.get("image")
        img=img.split('/')
        img=img[2]
        p=UploadedContent(user=user,caption=caption,post=img)
        p.save()
        return render(request,"upload_button/del.html",{'user':user,'caption':caption,'img':img})
    
    elif (request.method=="POST" and request.FILES['myfile']):
       f=request.FILES["myfile"]
       fs = FileSystemStorage()
       filename=fs.save(f.name,f)
       uploaded_file_url = fs.url(filename)
       return render(request,"upload_button/upload.html",{"upload_url":uploaded_file_url,"forms":form})
    
    return render(request,"upload_button/button_upload.html")

def upload_form(request):
    return HttpResponse("<h2>hello</h2>")