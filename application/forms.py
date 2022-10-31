from django import forms

class ApplicationForm(forms.Form):
    job_id = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Job ID', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    