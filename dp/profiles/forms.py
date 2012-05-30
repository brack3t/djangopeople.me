import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions

from profiles.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset("Configure your profile",
                "available_for",
                "location",
                "github_username",
                "bitbucket_username",
                "twitter_username",
                "linkedin_username",
                "anonymous_messages",
                "bio",
                "tags",
            ),
            FormActions(
                Submit("save", "Save", css_class="bttn btn-success")
            )
        )
        super(UserProfileForm, self).__init__(*args, **kwargs)
