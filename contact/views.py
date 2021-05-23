from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import  ContactForm

# Create your views here.
def contact(request):
    contact_form= ContactForm()
    if request.method=="POST":
        # recupero los datos del formulario 
        contact_form= ContactForm(data=request.POST)
        # valido los datos
        if contact_form.is_valid():
            name=request.POST.get('name','')
            mail=request.POST.get('mail','')
            content=request.POST.get('content','')
            # creamos el correo 
            mail=EmailMessage(
                "La Sabrosa: Nuevo mensaje de contacto",#Asunto
                "De {} {}\n\nEscribió:\n\n{}".format(name,mail,content),#mensaje
                "lasabrosa.com",#Email de Origen
                ["juanorlando1377@gmail.com"],#Email de destino
                reply_to=[mail]
            )
            #lo enviamos y redireccionamos
            try:
                mail.send()
                # todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha  ido bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")
            
    return render(request, 'contact/contact.html',{'form':contact_form})
# ver el video 8
