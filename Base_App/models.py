from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Item/')

    def __str__(self):
        return self.Item_name



class Aboutus(models.Model):
    Description = models.TextField(blank=False)


class Feedback(models.Model):
    User_name = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='Item/',blank=True)

    def __str__(self):
        return self.User_name


class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    Phoe_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name