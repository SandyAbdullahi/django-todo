from django import forms
from .models import List

class ListForm(forms.ModelForm):
    # user = forms.CharField(max_length=100, required=False, widget=forms.HiddenInput(), initial=1)
    list_name = forms.CharField(label="List Name", max_length=100)




    class Meta:
        model = List
        fields = ("user","list_name", "list_description")
