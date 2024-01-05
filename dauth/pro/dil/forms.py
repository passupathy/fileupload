from django import forms

class good(forms.Form):
    car=forms.CharField(widget=forms.TextInput (attrs={'class':'form-control'}))
    bus=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))