from django import forms


class CompanyForm(forms.Form):
    name = forms.CharField()
    description = forms.Textarea()
    established_date = forms.DateTimeField()
    location = forms.CharField()
    corporation_type = forms.CharField()
    social_media = forms.URLField()
    company_size = forms.IntegerField()
    logo = forms.URLField()

    def __str__(self):
        return self.name
    