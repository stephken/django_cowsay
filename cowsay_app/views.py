from django.shortcuts import render
from cowsay_app.forms import AddTxtForm
from cowsay_app.models import Txt

# Create your views here.


def index_view(request):
    form = AddTxtForm()
    if request.method == 'POST': 
            form = AddTxtForm(request.POST)
            if form.is_valid():
                form.save()
                form = AddTxtForm()
    return render(request, 'index.html', {'form': form})
    
