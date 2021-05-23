from django  import forms
# creo mi formulario de django
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs ={'class':'form-control','placeholder':'Nombre'}
    ))
    mail = forms.EmailField(required=True,widget=forms.EmailInput(
        attrs ={'class':'form-control','placeholder':'Correo Electronico'}
    ))
    content=forms.CharField(required=True, widget=forms.Textarea(
        attrs ={'class':'form-control','placeholder':'Deje su comentario'}
    ))