from multiprocessing import context
from django.shortcuts import render

from .models import Order, status_choice, Category

from django.db.models import Q

from django.core.serializers import serialize


def orderManagement(request):
    complete = Order.objects.filter(status='Complete')
    incomplete = Order.objects.exclude(status='Complete')
    complete_orders = []
    incomplete_orders = []
    categories = Category.objects.all()
    orders_by_category = {}
    # for category in categories:
    #     # Filtering
    #     key = f'{category.name} complete'
    #     value = (Order.objects.filter(Q(category=category.id), Q(status='Complete')))
    #     orders_by_category[key] = value
    #     key2 = f'{category.name} incomplete'
    #     value2 = (Order.objects.filter(Q(category=category), Q(status='Confirmed') | Q(status='Deleted')))
    #     orders_by_category[key2] = value2
        
    # print(orders_by_category)

    category_tree_complete = []
    category_tree_incomplete = []
    for category in categories:
        orders = Order.objects.filter(Q(category=category.id), Q(status='Complete'))
        children = []
        for order in orders:
            child = {'id': order.id, 'label': order.product}
            children.append(child)
        # key = f'{category.name} complete'
        # value = {'id': category.name, 'label': category.name, 'children': orders_by_category.get(f'{category.name} complete')}
        value = {'id': f'{category.name}-complete', 'label': f'{category.name}({len(children)})', 'children': children}
        category_tree_complete.append(value)
        orders2 = Order.objects.filter(Q(category=category), Q(status='Confirmed') | Q(status='Deleted'))
        children2 = []
        for order in orders2:
            child = {'id': order.id, 'label': order.product}
            children2.append(child)
        # key2 = f'{category.name} incomplete'
        value2 = {'id': f'{category.name}-incomplete', 'label': f'{category.name}({len(children2)})', 'children': children2}
        # value2 = {'id': category.name, 'label': category.name, 'children': orders_by_category.get(f'{category.name} incomplete')}
        category_tree_incomplete.append(value2)
        # print(orders)
        # print(orders2)

    # print(category_tree_complete)
    # print(category_tree_incomplete)
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
            'children': category_tree_complete,

        },
            {
            'id': 'incomplete',
            'label': f'Incomplete Orders ({len(incomplete_orders)})',
            'children': category_tree_incomplete
        }],
    }
    # print(order_tree)
    orders = Order.objects.all()
    # print(orders)
    context = {
        'orders': orders,
        'order_tree': order_tree
    }
    return render(request, 'new.html', context)



def modal(request):
    return render(request, 'modal.html',{})