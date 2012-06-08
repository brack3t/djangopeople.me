import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, HTML
from crispy_forms.bootstrap import FormActions


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
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
            "class": "input-small"
        })
    )
    units = forms.ChoiceField(
        choices=(
            ("km", "km"),
            ("mi", "mi")
        ),
        label='',
        widget=forms.Select(attrs={
            "class": "input-small"
        })
    )
    skills = forms.CharField(
        help_text="Enter comma-separated skills",
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
            "location",
            Div(
                HTML('<label for="id_distance" class="control-label '
                     'requiredField">Distance*</label><br>'),
                Div(
                    Field("distance", template="bootstrap/custom-field.html"),
                    Field("units", template="bootstrap/custom-field.html"),
                    css_class="controls"
                ),
                css_class="clearfix control-group"
            ),
            "skills",
            FormActions(
                Submit("search", "Search", css_class="btn btn-info"),
            )
        )
        super(SearchForm, self).__init__(*args, **kwargs)
