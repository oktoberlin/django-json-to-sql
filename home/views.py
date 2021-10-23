from django.shortcuts import render
from .models import Importjsondwisql

def index(request):
    data_dwi = Importjsondwisql.objects.all()
    print(data_dwi)
    return render(request, 'index.html', {'data_dwi':data_dwi})
