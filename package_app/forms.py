from django import forms


class Form(forms.Form):
    # id = forms.CharField(max_length=10)
    service = forms.MultipleChoiceField(choices=[("domain", "Domain"), ("internet", "Internet"), ("hosting", "Hosting")], widget=forms.CheckboxSelectMultiple())
    # price =
    addon = forms.MultipleChoiceField(choices=[("online bill pay", "Online Bill Pay"), ("real IP", "Real IP"), ("24/7 support", "24/7 Support")], widget=forms.CheckboxSelectMultiple())