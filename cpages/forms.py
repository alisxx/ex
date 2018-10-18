from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(
            required=True, 
            label='Email'
            )
    full_nm = forms.CharField(
            required=True, 
            label='Name'
            )
    org_nm = forms.CharField(
            required=True, 
            label='Organization'
            )
    ph_nbr = forms.CharField(
            required=True, 
            label='Contact number'
            )
    msg_text = forms.CharField(
            required=False, 
            label='Comments and Inquiries',
            widget=forms.Textarea
            )