from django.shortcuts import render,redirect

# Create your views here.
from .models import Post,Item,Branch,Transactions,Inventory
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

def inventory(request):
    '''if request.user.is_authenticated:
        user = request.user
    else:
        return  render(request,'login.html')'''
    if request.method == 'POST':
        if request.POST.get('item_name') and request.POST.get('item_quantity') and request.POST.get('branch'):
            inventory=Inventory()
            inventory.Item_Name= request.POST.get('item_name')
            inventory.Item_Quantity= request.POST.get('item_quantity')
            inventory.branch=request.POST.get('branch_code')
            inventory.save()

            return redirect('/')  

    else:
        return render(request,'inventory.html')


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
        #extract Information
        t_item_id = request.POST.get('Item_Id')
        t_source_branch = request.POST.get('Source_Branch')
        t_destination_branch = request.POST.get('Destination_Branch')
        t_quantity = request.POST.get('Quantity')
        t_type = request.POST.get('Transaction_Type')
        if t_item_id and t_source_branch and t_destination_branch and t_quantity:
            transaction = Transactions()
            transaction.Item_Id = t_item_id
            transaction.Source_Branch = t_source_branch
            transaction.Destination_Branch = t_destination_branch
            transaction.Quantity = t_quantity
            transaction.save()

            source_inventory = Inventory.objects.get(branch_Branch_Code=t_source_branch, item_id=t_item_id)
            destination_inventory = Inventory.objects.get(branch_Branch_Code=t_destination_branch, item_id=t_item_id)
            if request.POST.get('Transaction_Type') == 'DEBIT':
              source_inventory.quantity -= t_quantity
              destination_inventory.quantity += t_quantity
            else:
              source_inventory.quantity += t_quantity
              destination_inventory.quantity -= t_quantity
            source_inventory.save()
            destination_inventory.save()
            return redirect('/')  

    else:
        return render(request,'transaction.html')

