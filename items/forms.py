from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": (
                    "w-full text-green-700 border border-gray-300 rounded-lg p-2 "
                    "cursor-pointer file:bg-green-100 file:border-0 file:rounded file:px-4 "
                    "file:py-2 file:text-green-700 file:font-semibold hover:file:bg-green-200 "
                    "focus:outline-none focus:ring-2 focus:ring-green-400"
                )
            }
        )
    )

    class Meta:
        model = Item
        fields = ("name", "description", "date_found", "location", "status", "post_type", "image")
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400",
                "placeholder": "Item name"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400",
                "rows": 4,
                "placeholder": "Describe the item"
            }),
            "location": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400",
                "placeholder": "Location"
            }),
            "date_found": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400"
            }),
            "status": forms.Select(attrs={
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400"
            }),
            "post_type": forms.Select(attrs={
                "class": "w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-green-400"
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Only the user who posted can change status
        if self.instance and self.instance.pk and self.instance.found_by != user:
            self.fields.pop('status', None)