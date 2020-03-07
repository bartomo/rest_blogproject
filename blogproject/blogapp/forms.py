from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(label='title', initial='タイトル')
    content = forms.CharField(label='content', initial='本文（必須）', widget=forms.widgets.Textarea)
    category = forms.CharField(label='category')
    user_name = forms.CharField(label='user_name')


class SearchForm(forms.Form):
    # title_query = forms.CharField(label='title_query', initial='完全一致テスト')
    # category_query = forms.CharField(label='category_query', initial='test')
    user_name_query = forms.CharField(label='user_name_query')
