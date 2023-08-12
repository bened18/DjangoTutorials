from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django import forms 
# Create your views here.

class HomePageView(TemplateView): 
    template_name = "pages/home.html"

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs): 
            context = super().get_context_data(**kwargs) 
            context.update({ 
                "title": "About us - Online Store", 
                "subtitle": "About us", 
                "description": "This is an about page ...", 
                "author": "Developed by: Your Name", 
            }) 
            return context
    
class ContactPageView(TemplateView):
     template_name = "pages/contact.html"
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context.update({
               "title": "Contact us - Online Store", 
                "subtitle": "Contact us", 
                "email": "email: onlinestore@gmail.com", 
                "address": "address: Roadway 31st 50-3south",
                "phone_number": "phone number: +1 489023403",
          })
          return context

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Description: Best TV", "price":"1000"}, 
        {"id":"2", "name":"iPhone", "description":"Description: Best iPhone", "price":"1000"}, 
        {"id":"3", "name":"Chromecast", "description":"Description: Best Chromecast", "price":"100"}, 
        {"id":"4", "name":"Glasses", "description":"Description: Best Glasses", "price":"50"} 
    ] 

class ProductIndexView(View): 
    template_name = 'products/index.html' 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
        return render(request, self.template_name, viewData) 

 
class ProductShowView(View): 
    template_name = 'products/show.html'
    def get(self, request, id):
        try:
            if 1 <= int(id) <= len(Product.products): 
                viewData = {}
                Product.products[int(id)-1]
                product = Product.products[int(id)-1] 
                product['price'] = float(product['price'])
                viewData["title"] = product["name"] + " - Online Store" 
                viewData["subtitle"] =  product["name"] + " - Product information" 
                viewData["product"] = product 
                return render(request, self.template_name, viewData)
            else:
                 return HttpResponseRedirect(reverse('home'))
        except ValueError:
            return HttpResponseRedirect(reverse('home'))

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

 

class ProductCreateView(View): 
    template_name = 'products/create.html' 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 

    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            return redirect('product_created')  
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)