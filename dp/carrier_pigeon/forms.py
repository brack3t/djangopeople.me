import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div
from crispy_forms.bootstrap import FormActions

from carrier_pigeon.models import Message


class ContactForm(forms.ModelForm):

    class Meta:
        model = Message

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                Div(
                    Fieldset("Your Contact Info",
                        "name",
                        "email"
                    ),
                ),
                Div(
                    Fieldset("Message",
                        "subject",
                        "body"
                    ),
                ),
            css_class="row-fluid"
            ),
            FormActions(
                Submit("send", "Send", css_class="btn btn-success"),
            )
        )
        super(ContactForm, self).__init__(*args, **kwargs)