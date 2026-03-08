from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ("name", "description", "date_found", "location")

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-green-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-400",
                    "placeholder": "Item name",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "w-full border border-green-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-400",
                    "rows": 4,
                    "placeholder": "Describe the item",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "w-full border border-green-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-400",
                    "placeholder": "Where was it found?",
                }
            ),

            "date_found": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full border border-green-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-400",
                }
            ),
        }