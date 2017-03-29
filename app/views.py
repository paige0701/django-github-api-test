from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render
import json
import requests

def index(request):
    return HttpResponse('hello world')

def test(request):
    return HttpResponse('This is test')

def search(request):
    return render(request, 'app/search.html')

def profile(request):
    # req = requests.get('https://api.github.com/users/paige0701')
    # content = req.text
    # return render(request, 'app/profile.html')
    jsonList = []
    if request.method =='POST':
        user = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + user)
        jsonList.append(json.loads(req.text))
        parsedData = []
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
            parsedData.append(userData)

            context = {'userData': userData}
            return render(request,'app/profile.html', context)


