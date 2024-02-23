from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
import json
# Create your views here.


def returnPosts(code):
    values = {
        'abc123':{
            "1":{
                "title":"this is the title 1",
                "content":"this is the content",
                "likes":4
                },
            "2":{
                "title":"this is the title 2",
                "content":"content for 2nd",
                "likes":12
            }
        },
        'abc111':{
            "3":{
                "title":"this is the title 3",
                "content":"this is the content",
                "likes":12
                },
            "4":{
                "title":"this is the title 4",
                "content":"content for 2nd",
                "likes":32
            }
        }
    }
    return values[code] if code in values else None

def returnComments(code,id):
    values = {
        "abc123":{
            "1":{
                "1":"comment 1",
                "2":"comment 2"
            },
            "2":{
                "3":"comment 1",
                "4":"comment 2"
            }
        },
        "abc111":{
            "3":{
                "5":"comment 1",
                "6":"comment 2"
            },
            "4":{
                "7":"comment 1",
                "8":"comment 2"
            }
        }
    }
    if code in values and id in values[code]:
        return values[code][id]
    else:
        return None

@login_required
def home(request):
    code = request.user.username
    url = f"api/endpoint/{code}"
    # Code to fetch data from the api
    # response = requests.get(url=url)
    # data = json.dumps(response.text)
    data = returnPosts(code)
    return render(request,'dashboard/home.html',{'data':data})

@login_required
def comments(request,id):
    code = request.user.username
    url = f"api/endpoint/{code}/comments/{id}"
    # Code to fetch data from the api
    # response = requests.get(url=url)
    # data = json.dumps(response.text)
    data = returnComments(code,id)
    print(data)
    return render(request,'dashboard/comments.html',{'data':data})

@login_required
def createpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        opdatetime = request.POST.get('opdatetime')
        opimage = request.FILES.get('opimage')
        form_data = {"account":request.user.username,"title":title,"content":content}
        if opdatetime:
            form_data['schedule'] = opdatetime
        url ="api/endpoint/create/"
        # logic to send api request to create a new post
        # if opimage:
        #     response = requests.post(url, data=form_data, files={'image': opimage})
        # else:
        #     response = requests.post(url,data= form_data)
        # if response.ok:
        #     messages.success(request,"The post generated successfully")
        #     return redirect('home')
        # else:
        #     messages.error(request,'The post not generated please try again')
        #     return redirect('createpost')
        messages.success(request,"The post generated successfully")
        return redirect('home')

    return render(request,'dashboard/create_post.html')