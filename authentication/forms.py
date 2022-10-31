from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'style': 'width: 450px; height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    job_title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Current Job Title',
               'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}),
        label='')

    social_media = forms.URLField(widget=forms.URLInput(
        attrs={'placeholder': 'GitHub URL',
               'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}),
        label='')

    portfolio = forms.URLField(widget=forms.URLInput(
        attrs={'placeholder': 'Portfolio',
               'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}),
        label='')

    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'About','style': 'width: 450px;  height: 250px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 450px; height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'style': 'width: 450px;  height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 450px; height: 50px; display: block; padding: 20px 10px; margin: 10px auto; border: 1px solid #ccc; border-radius: 5px;'}), label='')
