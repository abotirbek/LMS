from django import forms


class StudentForm(forms.Form):
    # CustomUser fields
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    avatar = forms.ImageField(required=False)

    # StudentProfile fields
    birth_date = forms.DateField(required=False)
    parent_phone = forms.CharField(max_length=20)

    def __init__(self, *args, user_instance=None, profile_instance=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_instance = user_instance
        self.profile_instance = profile_instance

        if user_instance:
            self.fields['username'].initial = user_instance.username
            self.fields['first_name'].initial = user_instance.first_name
            self.fields['last_name'].initial = user_instance.last_name
            self.fields['email'].initial = user_instance.email
            self.fields['phone'].initial = user_instance.phone
            self.fields['avatar'].initial = user_instance.avatar

        if profile_instance:
            self.fields['birth_date'].initial = profile_instance.birth_date
            self.fields['parent_phone'].initial = profile_instance.parent_phone

    def save(self):
        # Save CustomUser
        user = self.user_instance
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        avatar = self.cleaned_data.get('avatar')
        if avatar:
            user.avatar = avatar

        user.save()

        # Save StudentProfile
        profile = self.profile_instance
        profile.birth_date = self.cleaned_data['birth_date']
        profile.parent_phone = self.cleaned_data['parent_phone']
        profile.save()

        return profile