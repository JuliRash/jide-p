from django.shortcuts import render

from django.http import HttpResponse

from contract.models import Contract


def index(request):
    contracts = Contract.objects.all()
    context = {'contracts': contracts}
    return render(request, 'index.html', context)


def add_contract(request):
    contracts = Contract.objects.get()
    context = {'contracts': contracts}
    return render(request, 'add_contract.html')
