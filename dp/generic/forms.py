import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Div, Field, MultiField
from crispy_forms.bootstrap import FormActions


class SearchForm(forms.Form):
    location = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class": "search-query",
                "placeholder": "Enter a location"
            }
        ),
    )
    distance = forms.IntegerField(
        initial=50,
        label='',
        widget=forms.NumberInput(attrs={
            "min": 1,
            "max": 6000,
        })
    )
    units = forms.ChoiceField(
        choices=(
            ("km", "km"),
            ("mi", "mi")
        ),
        label=''
    )
    skills = forms.CharField(
        help_text="Enter comma-separated skills",
        label='',
        widget=forms.TextInput(
            attrs={
                "class": "skills",
                "placeholder": "django, vim, redis"
            }
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = "form-inline"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Fieldset("Location", "location"),
            MultiField("Distance",
                Field("distance", css_class="input-small"),
                Field("units", css_class="input-small"),
                css_class="row-fluid"
            ),
            Fieldset("Skills", "skills"),
            FormActions(
                Submit("search", "Search", css_class="btn btn-info"),
            )
        )
        super(SearchForm, self).__init__(*args, **kwargs)
