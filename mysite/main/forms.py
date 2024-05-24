from django import forms
from .models import JournalEntry
class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length = 200)
    check = forms.BooleanField(required = False)



class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['entry_title', 'entry_date', 'entry_content']
