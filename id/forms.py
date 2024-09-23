from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

USER = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=16,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        min_length=8,
        max_length=32,
        label="Password",
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not password or not username:
            raise forms.ValidationError("Form is not valid. Try again!")

        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError("Wrong username or/and password. Try again!")

        self.user = user

        return cleaned_data


class CreateUserForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=32,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    first_name = forms.CharField(
        label="First name",
        max_length=32,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=32,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email address",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        min_length=8,
        max_length=32,
        label="Password",
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if any(
            elem is None or len(str(elem)) == 0
            for elem in [username, first_name, last_name, email, password]
        ):
            raise forms.ValidationError("Form is not valid. Try again!")

        # check if username or email is already taken
        if USER.objects.all().filter((Q(username=username) | Q(email=email))):
            raise forms.ValidationError("User already exists!")

        return cleaned_data

    def save(self):
        username = self.cleaned_data["username"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        try:
            user = USER.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)
            raise forms.ValidationError("Something went wrong. Try again.")
