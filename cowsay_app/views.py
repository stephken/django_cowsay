from django.shortcuts import render
from cowsay_app.forms import AddTxtForm
from cowsay_app.models import Txt
from subprocess import check_output

# Create your views here.


def index_view(request):
    form = AddTxtForm()
    if request.method == 'POST': 
            form = AddTxtForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                txt = form.cleaned_data.get('user_input')
                form.save()
                return render(request, 'index.html', {'form': form, 'output': check_output(['cowsay', txt]).decode('utf-8')})
    form = AddTxtForm()
    return render(request, 'index.html', {'form': form})
    
