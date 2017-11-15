from django.conf.urls import url
from ngaraapp import views

urlpatterns = [
   url(r'^$', views.HomePageView.as_view()),
   url(r'^service/$', views.ServicePageView.as_view()),
   url(r'^about/$', views.AboutPageView.as_view()),
   url(r'^contact/$', views.ContactPageView.as_view()),
  # url(r'^contact/$', views.Contact),
  
   
   # url(r'^form/$', views.MyModelAdmin.as_view()),
]
