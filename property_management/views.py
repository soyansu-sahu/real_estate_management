from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Property, Unit, Tenant

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.get_full_name()}")
                return redirect('property_listing')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

@login_required
def property_listing(request):
    properties = Property.objects.all()
    return render(request, 'property_listing.html', {'properties': properties})

@login_required
def property_profile(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    units = Unit.objects.filter(property=property_obj)
    return render(request, 'property_profile.html', {'property': property_obj, 'units': units})

@login_required
def tenant_profile(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    return render(request, 'tenant_profile.html', {'tenant': tenant})

@login_required
def property_search(request):
    if request.method == 'POST':
        unit_type = request.POST.get('unit_type')
        location = request.POST.get('location')
        
        units = Unit.objects.filter(unit_type=unit_type, property__location=location)
        return render(request, 'property_search.html', {'units': units})
    return render(request, 'property_search.html')
