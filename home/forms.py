from django import forms

from .models import People


class Peopleform(forms.ModelForm):
    class Meta:
        model = People
        fields = [
            'id',
            'name',
            'instagram',
            'snapchat',
            'others',
        ]
