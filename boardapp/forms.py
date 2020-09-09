from django import forms
from .models import DjangoBoard

class DjangoBoardForm(forms.ModelForm):
    class Meta:
        model = DjangoBoard
        fields = ['subject','professor','item','year','title','upload_files']

        widgets = {
            'subject' : forms.TextInput(attrs={'class':'board_form'}),
            'professor' : forms.TextInput(attrs={'class':'board_form'}),
            'upload_files' : forms.FileInput(attrs={'class':'board_form',}),
            'title' : forms.TextInput(attrs={'class':'board_form'}),
            'year' : forms.NumberInput(attrs={'class':'board_form'}),
        }