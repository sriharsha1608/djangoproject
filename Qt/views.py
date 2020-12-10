from django.shortcuts import render,redirect

# Create your views here.
from .models import Post,Item,Branch,Quantity,Transactions
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
#@login_required
def createpost(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request,'createpost.html')
    else:
        return  render(request,'login.html')
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
                
            return redirect('/')  

    else:
        return render(request,'createpost.html')
        
    

def nlrdetail(request):
    result=Post.objects.all()
    return render(request,"nlrdetail.html",{"Post":result})

def quantity(request):
    '''if request.user.is_authenticated:
        user = request.user
    else:
        return  render(request,'login.html')'''
    if request.method == 'POST':
        if request.POST.get('item_name') and request.POST.get('Item_Quantity'):
            quantity=Quantity()
            quantity.Item_Name= request.POST.get('Item_Name')
            quantity.Item_Quantity= request.POST.get('Item_Quantity')
            quantity.save()

            return redirect('/')  

    else:
        return render(request,'quantity.html')


def branch(request):
    '''if request.user.is_authenticated:
        user = request.user
    else:
        return  'Please <a href="accounts/login">Login</a>' '''
    if request.method == 'POST':
        if request.POST.get('Branch_code') and request.POST.get('Branch_Name') and request.POST.get('Branch_Addres'):
            branch=Branch()
            branch.Branch_code = request.POST.get('Branch_code')
            branch.Branch_Name = request.POST.get('Branch_Name')
            branch.Branch_Addres = request.POST.get('Branch_Addres')
            branch.save()

            return redirect('/')

    else:
        return render(request,'branch.html')

def item(request):
    '''if request.user.is_authenticated:
        user = request.user
    else:
        return  'Please <a href="accounts/login">Login</a>' '''
    if request.method == 'POST':
        if request.POST.get('Item_Name'):
            item=Item()
            item.Item_Name = request.POST.get('Item_Name')
            
            item.save()

            return redirect('/')

    else:
        return render(request,'item.html')

def transaction(request):
    if request.method == 'POST':
        if request.POST.get('Item_Id') and request.POST.get('Source_Branch') and request.POST.get('Destination_Branch') and request.POST.get('Quantity'):
            transaction = Transactions()
            transaction.Item_Id = request.POST.get('Item_Id')
            transaction.Source_Branch = request.POST.get('Source_Branch')
            transaction.Destination_Branch = request.POST.get('Destination_Branch')
            transaction.Quantity= request.POST.get('Quantity')
            transaction.save()
            return redirect('/')  

    else:
        return render(request,'transaction.html')


