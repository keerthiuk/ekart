from django.shortcuts import redirect, render

from seller.models import Seller
from .models import Customer
# Create your views here.


def customer_home(request):
    return render(request, 'customer/customer_home.html')


def store(request):
    return render(request, 'customer/store.html')


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    message = ""
    if request.method == 'POST':  
        fname = request.POST['first_name'] 
        lname = request.POST['last_name']        
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        companyname = request.POST['company-name']
        bank_name = request.POST['bank-name']
        branch_name = request.POST['branch-name']
        account_no = request.POST['account-number']
        ifsc = request.POST['ifsc']
        profile_pic = request.FILES['profile-pic']
        
        seller_exist = Seller.objects.filter(email = email).exists()
        
        if not seller_exist:
            seller = Seller(
                first_name = fname, 
                last_name = lname ,
                company_name = companyname, 
                gender = gender, 
                email = email,
                city = city, 
                country = country, 
                account_no=account_no,
                bank_name=bank_name, 
                branch_name=branch_name, 
                ifsc=ifsc,
                pic=profile_pic
                )
            seller.save()
            message = 'Registration Succesful'

        else:
            message = 'Email already exists'
    
    return render(request, 'customer/seller_register.html',{"status":message})


def seller_login(request):
    message =''
    if request.method == 'POST':
        c_seller_id = request.POST['seller_id'] 
        c_password = request.POST['password']
        
        new_seller = Seller.objects.filter(email = c_seller_id, password = c_password)
        #filter(name the table)
                
        if new_seller.exists():
            print(new_seller)
            # print('before redirect')
            request.session['seller'] = new_seller[0].id
            return redirect('seller:seller_home')
        else:
            # print('inside else block')
            message = 'incorrect password or username'
    
    
    return render(request, 'customer/seller_login.html',{'status':message})


def customer_signup(request):
    message = ""
    if request.method == 'POST':  
        fname = request.POST['fname'] 
        lname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']
        
        customer_exist = Customer.objects.filter(email = email).exists()
        
        if not customer_exist:
            customer = Customer(first_name = fname, last_name = lname , gender = gender, email = email, 
                            city = city, country = country, password = password)
            customer.save()
            message = 'Registration Succesful'

        else:
            message = 'Email already exists'
            
    return render(request, 'customer/customer_signup.html',{"status":message})


def customer_login(request):
    message =''
    if request.method == 'POST':
        c_username = request.POST['email'] 
        c_password = request.POST['password']
        
        new_customer = Customer.objects.filter(email = c_username, password = c_password)
        #filter(name the table)
                
        if new_customer.exists():
            print(new_customer)
            # print('before redirect')
            request.session['customer'] = new_customer[0].id
            return redirect('customer:customer_home')
        else:
            # print('inside else block')
            message = 'incorrect password or username'
    
    return render(request, 'customer/customer_login.html',{"status":message})



def forgot_password_customer(request):
    
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')