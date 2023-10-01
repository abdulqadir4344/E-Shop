from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from .models.customer import Customer
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    
    if request.method =="POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:

                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('homepage')




    else:

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are : ' , request.session.get('email'))
        return render(request,'index.html', data)




@csrf_exempt
def validateCustomer(customer):
    error_message = None

    if(not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required !'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more' 
    elif not customer.phone :
        error_message = 'Phone Number Required'
    elif len(customer.phone) < 10 :
        error_message = "Phone Number must be 10 char long"  
    elif len(customer.password) < 6:
        error_message = "Password must be 6 char long"
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExists():
        error_message = 'Email Address Already Registered !'
        #saving

    return error_message




#For Signup
@csrf_exempt 
def signup( request):
    if request.method == "GET":
        return render(request,'signup.html') 

    else: 
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #Validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name ,
                            last_name=last_name , 
                            phone=phone, 
                            email=email , 
                            password=password)

        error_message=validateCustomer(customer)

            
       

        if not error_message:

            print(first_name , last_name , phone , email , password)
            customer.password = make_password(customer.password)
            customer.register()
           

            return redirect('homepage')
            
        else:
            data = {
                'error':error_message,
                'values':value
            }

            return render(request , 'signup.html', data)
        
              


    


from django.shortcuts import render , redirect ,  HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from django.views.decorators.csrf import csrf_exempt




#For Login


    
@csrf_exempt 
def login(request):
    return_url = None
    login.return_url = request.GET.get('return_url')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if login.return_url:
                    return HttpResponseRedirect(login.return_url)
                else:
                    login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        print(email , password)
        print('you are : ' , request.session.get('email'))
        return render(request, 'login.html' , {'error': error_message}) 

    else:
        
        return render(request , 'login.html')

@csrf_exempt 
def logout(request):
    request.session.clear()

    return redirect('login')

from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


from django.views.decorators.csrf import csrf_exempt




#For Login
@csrf_exempt
def OrderView(request):
    
    if request.method=="GET":

        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        orders = orders.reverse()
        print(orders)
        return render(request , 'orders.html', {'orders':orders})


from django.shortcuts import render , redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.views.decorators.csrf import csrf_exempt




# Create your views here.



from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from store.models.product import Product
from store.models.orders import Order
from django.views.decorators.csrf import csrf_exempt




#For Login
@csrf_exempt
def checkout(request):
    
    if request.method=="POST":

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address , phone , customer , cart , products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id = customer),
                        product=product,
                        price=product.price ,
                        address=address , 
                        phone=phone , 
                        quantity=cart.get(str(product.id) )) 
            order.save()
        request.session['cart'] = {}
        return redirect('cart')

    else:
        return HttpResponseRedirect('login')
    



from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from store.models.product import Product
from django.views.decorators.csrf import csrf_exempt



#For Login
@csrf_exempt
def Cart(request):
    if request.method == "GET":
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products': products})
    

def profile(request):

    return render(request , 'profile.html')