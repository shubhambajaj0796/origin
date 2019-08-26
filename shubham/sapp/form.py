from django import forms


class RegistrationForm1(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=200)
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    contact = forms.CharField(label="Enter Your Contact", max_length=200)
    address = forms.CharField(label="Enter Your Address", max_length=200)
    password = forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)
    CHOICES=[('Male','Male'),('Female','Female'),('others','others')]

    Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class login(forms.Form):
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password = forms.CharField(label="Enter Your password", max_length=200)

class emp1(forms.Form):
    e_salary = forms.CharField(label="Enter Your salary", max_length=200)
    e_experience = forms.CharField(label="Enter Your experience", max_length=200)
    e_profile = forms.CharField(label="Enter Your profile", max_length=200)
