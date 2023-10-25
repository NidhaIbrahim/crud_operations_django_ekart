from django.shortcuts import redirect, render
from random import randint
from django.conf import settings
from django.core.mail import send_mail

from customer.models import Customer, Seller
# from .models import Customer
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
    msg = ''
    status = False
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        company_name = request.POST['companyname']
        bank_name = request.POST['bankname']
        bank_branch = request.POST['branch']
        account_number = request.POST['accnumber']
        ifsc = request.POST['ifsc']
        seller_image = request.FILES['picture']
        login_id = 'sell-' + f_name + '-'
        password = randint(111111, 999999)

        seller = Seller(
            first_name = f_name,
            last_name = l_name,
            email = email,
            gender = gender,
            city = city,
            country = country,
            seller_picture = seller_image,
            company_name = company_name,
            bank_name = bank_name,
            bank_branch = bank_branch,
            account_number = account_number,
            ifsc = ifsc,
            login_Id = login_id,
            password = password
        )

        seller.save()
        msg = 'Account created successfully'
        email_subject = 'Login Credentials'
        email_content = f"Welcome {f_name} {l_name}. Your username will be {login_id} and password will be {password}."

        send_mail(
            email_subject, 
            email_content,
            settings.EMAIL_HOST_USER, 
            [email]
        )

    return render(request, 'customer/seller_register.html', { 'message' : msg })


def seller_login(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['seller_id']
        s_password = request.POST['seller_password']

        sellernew = Seller.objects.filter( login_Id = s_username, password = s_password )
        if sellernew.exists():
            request.session['seller'] = sellernew[0].id
            return redirect('Seller:seller_home')
        else:
            msg = ' Invalid Credentials ! '

    return render(request, 'customer/seller_login.html', {'message' : msg})


def customer_signup(request):
    msg = ''
    status = False
    if request.method == 'POST':
        f_name = request.POST['fname'] 
        l_name = request.POST['lastname'] 
        email = request.POST['email'] 
        gender = request.POST['gender'] 
        city = request.POST['city'] 
        country = request.POST['country'] 
        password = request.POST['password'] 

        customer_exist = Customer.objects.filter(email = email).exists()

        if not customer_exist:
            customer = Customer(
                first_name = f_name,
                last_name = l_name,
                email = email,
                gender = gender,
                city = city,
                country = country,
                password = password
                )
            
            customer.save()
            msg = ' Registeration successfull! '
            status = True
        else:
            msg = ' Already registered! '

    return render(request, 'customer/customer_signup.html', {'message' : msg, 'status' : status})


def customer_login(request):
    msg = ''
    if request.method == 'POST':
        c_email = request.POST['email']
        c_password = request.POST['password']

        customer = Customer.objects.filter(email = c_email, password = c_password)
        if customer.exists():
            request.session['customer'] = customer[0].id
            return redirect('customer:customer_home')
    
        else:
             msg = ' Invalid Credentials ! '

    return render(request, 'customer/customer_login.html', {'message' : msg})


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')
