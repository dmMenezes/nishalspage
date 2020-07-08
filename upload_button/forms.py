from django import forms


class user_content(forms.Form):
    user=forms.CharField(max_length=150)
    caption=forms.CharField(max_length=1000,required=False,widget=forms.Textarea)

