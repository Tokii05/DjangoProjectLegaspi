from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request,'helloWorld.html')

def testPath(request):
    return render(request,'testPath.html')
