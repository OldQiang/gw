from django.shortcuts import render
from django.http import  HttpResponse
import os

def upload_file(request):
    print("step 1")
    if request.method == "POST":    # 请求方法为POST时，进行处理
        print("step 2")
        print(request)
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            print("step 3")
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        print("step 4")
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")