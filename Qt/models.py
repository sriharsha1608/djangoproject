from django.db import models
import uuid



class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
# Create your models here.

class Item(models.Model):
    Item_Name = models.CharField(max_length=300, unique=True, null=True)
    id = models.AutoField(primary_key=True,unique=True, null=False)
    #Item_Size = models.CharField(max_length=300)

class Branch(models.Model):
    Branch_Code = models.CharField(max_length=300)
    Branch_Name = models.CharField(max_length=300)
    Branch_Addres = models.CharField(max_length=300)
    #id = models.AutoField(primary_key=True,unique=True, null=False)


class Inventory(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE,to_field='id',null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,to_field='id',null=True)
    quantity = models.IntegerField()


class Transactions(models.Model):
    Transactions_ID = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4)
    Item_Id = models.IntegerField(null=False)
    Source_Branch = models.CharField(max_length=300,null=False)
    Destination_Branch = models.CharField(max_length=300,null=False)
    Transaction_Type = models.CharField(max_length=300,null=False)
    Quantity = models.IntegerField(null=False)
    
