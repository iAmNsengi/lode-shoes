from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    
    # to save the datas
    def register(self):
        self.save()

    @staticmethod
    def get_client_by_username(username):
        try:
            return Client.objects.get(username = username)
        except:
            return False
    @staticmethod
    def get_client_by_email(email):
        try:
            return Client.objects.get(email = email)
        except:
            return False
    def clientExist(self):
        if Client.objects.filter(email=self.email):
            return True
        return False    
    def __str__(self):
        return self.username

class ClientVerify(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    code = models.CharField(max_length = 6)


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    qty = models.IntegerField(default=1)
    description = models.TextField(null=True)
    image=models.ImageField(upload_to='products')

    def __str__(self):
        return self.name

STATUS = (
    (0,"Order Received"),
    (1,"Payment Received"),
    (2,"Delivered")
)

class Order(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    client= models.ForeignKey(Client,on_delete=models.CASCADE)
    quantity_ordered=models.IntegerField(default=1)
    shoe_size= models.IntegerField(default=42)
    amount = models.IntegerField(default=0)
    ship_address=models.CharField(max_length=100,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    proof = models.ImageField(upload_to='proofs/')
    order_status = models.IntegerField(choices=STATUS,default=0)
    comment = models.TextField(default="Upload your screenshot of your payment!" ,null=True,blank=True)

    def __str__(self):
        return self.client.username
    def get_total_price(self):
        return self.product.price * self.quantity_ordered

class Cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    shoe_size= models.IntegerField(default=42)
    amount = models.IntegerField(default=0,  null=True)

    def get_total_price(self):
        return self.item.price * self.quantity

    def __str__(self):
        return self.item.name
