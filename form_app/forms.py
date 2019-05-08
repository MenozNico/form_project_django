from django import forms
from .models import Message
from django.core import validators
from django.core.exceptions import ValidationError

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"

class FormContact(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Scrivi il testo qui!"}), validators=[validators.MinLengthValidator(10)])

    def clean_text(self):
        data = self.cleaned_data["text"]
        if "stronzo" in data:
            raise ValidationError("Il contenuto inserito viola le norme del sito")