from  Home.models import Home       

#proceso para recuperar telefonmo y corre del modelo home
def home_contact(request):
    home = Home.objects.latest('created')
    
    return{
        
        'phone': home.phone,
        'title': home.title,
    }