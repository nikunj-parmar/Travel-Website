from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    # name1 = input("Enter name: ")
    return render(request, 'home.html', {'name': "nik!"})


def calc(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    addition = request.POST.get('addition', 'off')
    multiply = request.POST.get('multiply', 'off')
    division = request.POST.get('division', 'off')

    if addition == "on":
        res = val1 + val2
        # params={'result':res}
        return render(request, "result.html", {'result': res})
    if multiply == "on":
        res = val1 * val2
        # params = {'result': res}
        return render(request, "result.html", {'result': res})
    if division == 'on':
        res = val1 / val2
        # params = {'result': res}
        return render(request, "result.html", {'result': res})

    # if (addition != "on" and multiply != "on" and division != "on"):

        # return HttpResponse("please select any operation and try again")

    # return render(request, "result.html", {'result': res})