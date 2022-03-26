from django import forms


class Form(forms.Form):
    service = forms.MultipleChoiceField(choices=[("domain", "Domain"), ("internet", "Internet"), ("hosting", "Hosting")], widget=forms.CheckboxSelectMultiple())
    addon = forms.MultipleChoiceField(choices=[("online bill pay", "Online Bill Pay"), ("real IP", "Real IP"), ("24/7 support", "24/7 Support")], widget=forms.CheckboxSelectMultiple())