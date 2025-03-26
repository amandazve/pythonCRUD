from django.forms import ModelForm
from app.models import Person

# Create the form class.
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['FirstName', 'LastName', 'Contact']