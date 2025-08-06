from django.shortcuts import render
from .models import SupportTicket

def my_tickets(request):
    tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, 'support/my_tickets.html', {'tickets': tickets})