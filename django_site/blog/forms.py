from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label = '제목',
        max_length = 100,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    text = forms.CharField(
        label = '내용',
        required = True,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control'
            }
        )
    )