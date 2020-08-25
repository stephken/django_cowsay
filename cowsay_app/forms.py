from django import forms
from cowsay_app.models import Txt



class AddTxtForm(forms.ModelForm):
    class Meta:
        model = Txt
        fields = ('user_input',)
        