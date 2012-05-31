import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div
from crispy_forms.bootstrap import FormActions


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "search-query",
                "placeholder": "Enter a location"
            }
        ),
    )
    distance = forms.IntegerField(
        initial=50,
        widget=forms.NumberInput(attrs={
            "min": 1,
            "max": 6000
        })
    )
    units = forms.ChoiceField(
        choices=(
            ("km", "km"),
            ("mi", "mi")
        )
    )
    skills = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "skills",
                "placeholder": "django, vim, redis"
            }
        ),
        required=False,
        help_text="Enter comma-separated skills"
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                Fieldset("Location",
                    "location",
                ),
                Fieldset("Distance",
                    "distance",
                    "units",
                    css_class="span3"
                ),
                Fieldset("Skills",
                    "skills",
                    css_class="span3"
                ),
                css_class="row-fluid"
            ),
            FormActions(
                Submit("search", "Search", css_class="btn btn-info"),
            )
        )
        super(SearchForm, self).__init__(*args, **kwargs)
