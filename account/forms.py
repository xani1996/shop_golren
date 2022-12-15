from django import forms
from django.contrib.auth.models import User

messages = {
    'required': 'لطفا این فیلد را پر کنید',
    'invalid': 'لطفا یک ایمیل معتبر وارد کنید',
    'min_length': 'تعداد کارکتر های ورودی کمتر از حد مجاز است',
    'max_length': 'تعداد کارکتر های ورودی بیشتر از حد مجاز است',
}


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput, error_messages=messages)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput, error_messages=messages)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
