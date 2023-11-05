from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('pay', views.make_payment, name='pay'),
    path('payment', views.order_payment, name='payment'),
    path('callback/', views.callback, name='callback'),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),



]
