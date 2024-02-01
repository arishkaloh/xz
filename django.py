pip install django
django - admin startproject myproject
cd myproject
python manage.py startapp myapp
python
INSTALLED_APPS = [
    ...
    'myapp',
]
python
   from django.shortcuts import render
   from django.contrib.admin.views.decorators import staff_member_required
   from django.views.decorators.cache import never_cache

   def homepage(request):
       return render(request, 'myapp/homepage.html')

   @staff_member_required
   @never_cache
   def adminpage(request):
       return render(request, 'myapp/adminpage.html')

   def styledpage(request):
       return render(request, 'myapp/styledpage.html')
html
{ % load
static %}
< !DOCTYPE
html >
< html >
< head >
< title > Homepage < / title >
< / head >
< body >
< h1 > Homepage < / h1 >
< p > Content: {{flatpage.content}} < / p >
< / body >
< / html >

- adminpage.html:

html
{ % load
static %}
< !DOCTYPE
html >
< html >
< head >
< title > Admin
Page < / title >
< style >
body
{
    font - size: 20px;
}
< / style >
< / head >
< body >
< h1 > Admin
Page < / h1 >
< p > Content: {{flatpage.content}} < / p >
< / body >
< / html >

- styledpage.html:
html
{ % load
static %}
< !DOCTYPE
html >
< html >
< head >
< title > Styled
Page < / title >
< link
href = "{% static 'css/bootstrap.min.css' %}"
rel = "stylesheet" >
< style >
body
{
    font - family: 'Arial', sans - serif;
font - size: 18
px;
}
< / style >
< / head >
< body >
< h1 > Styled
Page < / h1 >
< p > Content: {{flatpage.content}} < / p >
< / body >
< / html >

python
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('styledpage/', views.styledpage, name='styledpage'),
]
python manage.py runserver
