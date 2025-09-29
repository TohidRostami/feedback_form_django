from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your name",
        max_length=10,
        error_messages={
            "required": "Your name can't be empty!",
            "max_length": "Please enter a shorter name!",
        }
    )
