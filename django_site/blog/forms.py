from django import forms


class PostCreateForm(forms.Form):
    title_create = forms.CharField(
        label = '제목',
        max_length = 100,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    text_create = forms.CharField(
        label = '내용',
        required = True,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control'
            }
        )
    )


class PostModifyForm(forms.Form):
    title_modify = forms.CharField(
        label = '제목',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    text_modify = forms.CharField(
        label = '내용',
        required = True,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control'
            }
        )
    )