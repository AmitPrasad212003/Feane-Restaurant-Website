from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable,Aboutus,Feedback,ItemList,Items
# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request,'home.html',{'items': items,'list':list,'review': review})

def AboutView(request):
    data = Aboutus.objects.all()
    return render(request,'about.html',{'data': data})

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html', {'items': items,'list':list})

def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        Email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')
        if name != '' and Email != '' and phone_number != '' and len(phone_number) == 10 and  total_person != '' and booking_date != '':
            data = BookTable(Name = name, Phoe_number = phone_number, Email = Email, Total_person = total_person, Booking_date = booking_date)

            data.save()

    return render(request,'book_table.html')


def FeedbackView(request):
    return render(request,'feedback.html')
