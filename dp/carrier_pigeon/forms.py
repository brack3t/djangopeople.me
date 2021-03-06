import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions

from carrier_pigeon.models import Message


class ContactForm(forms.ModelForm):


    class Meta:
        model = Message

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)

        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Fieldset("Send me a message",
                "name",
                "email",
                "subject",
                "body"
            ),
            FormActions(
                Submit("send", "Send", css_class="btn btn-success"),
            )
        )
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields["recipient"].widget = forms.HiddenInput()
        self.fields["sender"].widget = forms.HiddenInput()

        if not user:
            self.fields["name"].required = True
            self.fields["email"].required = True

        if user:
            self.fields["name"].initial = user.first_name
            self.fields["name"].widget = forms.HiddenInput()
            self.fields["email"].initial = user.email
            self.fields["email"].widget = forms.HiddenInput()