from django.urls import path
from .views import home, about, contactus, thankyou,all_person,single_view,signup_view,login_view,logout_view
urlpatterns = [
path('logout/',logout_view,name='logout_url'),
path('login/',login_view,name='login_url'),
path('signup/',signup_view,name='signup_url'),
path('single/<int:id>/',single_view,name="single_url"),
path('all/',all_person,name="all_poerson_url"),
path('thankyou/',thankyou,name="thankyou_url"),
path('contactus/',contactus,name="contactus_url"),
path('about/',about,name="about_url"),
path('',home,name="home_url")

]
