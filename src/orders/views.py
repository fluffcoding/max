from multiprocessing import context
from django.shortcuts import render

from .models import Order, status_choice

from django.core.serializers import serialize


def orderManagement(request):
    orders = Order.objects.all()
    complete = Order.objects.filter(status='Complete')
    incomplete = Order.objects.exclude(status='Complete')
    complete_orders = []
    incomplete_orders = []
    for order in complete:
        complete_orders.append(
            {'id': order.id, 'label': f'{order.product} - {order.category}'})
    for order in incomplete:
        incomplete_orders.append(
            {'id': order.id, 'label': f'{order.product} - {order.category}'})
    order_tree = {
        'id': 'root',
        'children': [{
            'id': 'complete',
            'label': f'Complete Orders ({len(complete_orders)})',
            'children': complete_orders,

        },
            {
            'id': 'incomplete',
            'label': f'Incomplete Orders ({len(incomplete_orders)})',
            'children': incomplete_orders
        }],
    }
    context = {
        'orders': orders,
        'order_tree': order_tree
    }
    return render(request, 'new.html', context)
