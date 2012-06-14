import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div
from crispy_forms.bootstrap import FormActions

from profiles.models import UserProfile

class UserProfileForm(forms.ModelForm):
    username = forms.RegexField(label="Username", max_length=30,
        regex=r"^[\w.@+-]+$", help_text="30 characters or fewer. "
        "Letters, digits and @/./+/-/_ only.",
        error_messages = {
            "invalid": "This value may contain only letters, numbers and "
                "@/./+/-/_ characters."})
    email = forms.EmailField(label="Email", help_text="Email address you want "
        "to receive emails from us at. Leave blank if you don't want emails.",
        required=False)
    first_name = forms.CharField(label="Full Name")
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                Fieldset("Personal Details",
                    "first_name",
                    "username",
                    "email",
                    "gravatar_email",
                    "location",
                    "available_for",
                    "bio",
                    css_class="span6"
                ),
                Div(
                    Fieldset("Site Details",
                        "github_username",
                        "bitbucket_username",
                        "twitter_username",
                        "linkedin_username",
                        "anonymous_messages",
                        "tags",
                    ),
                    Fieldset("Location Details",
                        Div(id="map"),
                        "latitude",
                        "longitude"
                    ),
                    css_class="span6"
                ),
                css_class="row-fluid"
            ),
            FormActions(
                Submit("save", "Save", css_class="btn btn-success"),
            )
        )
        super(UserProfileForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            user = self.instance.user
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email
            self.fields["first_name"].initial = user.first_name
            self.fields["latitude"].initial = self.instance.coords[0]
            self.fields["longitude"].initial = self.instance.coords[1]

    def clean(self):
        """
        Shame user for messing with map data.
        """
        if not isinstance(self.data["latitude"], float) or not isinstance(
            self.data["longitude"], float):

            raise forms.ValidationError("Messing with map coordinates won't "
                "get you anywhere.")

        return super(UserProfileForm, self).clean()

    def save(self, *args, **kwargs):
        """
        Use lat/lng values to create a POINT on the instance.
        """
        self.instance.point = u"POINT(%f %f)" % (self.cleaned_data["longitude"],
            self.cleaned_data["latitude"])
        super(UserProfileForm, self).save(*args, **kwargs)
