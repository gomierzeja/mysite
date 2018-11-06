from django import forms

class SequencePostForm(forms.Form):
    sequence = forms.CharField()
    grammar = forms.CharField()
