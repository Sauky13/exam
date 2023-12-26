from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserForm, ServiceForm
from .models import CustomUser, Service, Order
from django.contrib import messages


def index(request):
    latest_services = Service.objects.order_by('-id')[:5]
    return render(request, 'main/index.html', {'latest_services': latest_services})


class LoginViewUser(LoginView):
    template_name = 'register/login.html'


def logout_view(request):
    logout(request)
    return render(request, 'register/logout.html')


@login_required
def profile(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'register/profile.html', {'user_orders': user_orders})


class UserRegister(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('main:register_done')


class RegisterDone(TemplateView):
    template_name = 'register/register_done.html'


def services(request):
    all_services = Service.objects.all()
    return render(request, 'main/service.html', {'services': all_services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'main/services_detail.html', {'service': service})


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:service')
    else:
        form = ServiceForm()

    return render(request, 'main/add_service.html', {'form': form})


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.user.is_superuser:
        service.delete()

    return redirect('main:service')


def order_service(request, service_id):
    if request.user.is_authenticated:
        service = get_object_or_404(Service, id=service_id)
        order = Order.objects.create(user=request.user)
        order.products.add(service)
        messages.success(request, f'Successfully ordered {service.name}!')
        return redirect('main:order_success')
    else:
        messages.error(request, 'You must be logged in to place an order.')
        return redirect('main:login')


def order_success(request):
    return render(request, 'main/order_success.html')


def search_services(request):
    query = request.GET.get('query', '')
    results = Service.objects.filter(name__icontains=query)

    return render(request, 'main/search_services.html', {'results': results, 'query': query})