# upload_app/forms.py
from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel/CSV file")
