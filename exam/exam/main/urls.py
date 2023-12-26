from django.conf import settings
from django.urls import path
from .views import index, LoginViewUser, logout_view, UserRegister, RegisterDone, profile, services, service_detail, \
    add_service, delete_service, order_service, order_success, search_services
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
                  path('', index, name='index'),
                  path('accounts/login', LoginViewUser.as_view(), name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('register/', UserRegister.as_view(), name='register'),
                  path('register/done/', RegisterDone.as_view(), name='register_done'),
                  path('accounts/profile/', profile, name='profile'),
                  path('service/', services, name='service'),
                  path('services/<int:service_id>/', service_detail, name='service_detail'),
                  path('add_service/', add_service, name='add_service'),
                  path('delete_service/<int:service_id>/', delete_service, name='delete_service'),

                  path('order/<int:service_id>/', order_service, name='order_service'),
                  path('order/success/', order_success, name='order_success'),
                  path('search/', search_services, name='search_services'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
