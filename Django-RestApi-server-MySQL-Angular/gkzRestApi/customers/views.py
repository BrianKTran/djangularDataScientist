from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from customers.models import Customer
from customers.serializers import CustomerSerializer


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def customer_list_age(request, age):
    customers = Customer.objects.filter(age=age)

    if request.method == 'GET':
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

def get(self, request, file_name):

    bicloudreposervice = BiCloudRepoService()

    file_obj = bicloudreposervice.get_user_file(request.user.email, file_name)
    file_path = file_obj.name

    with open(file_path, 'rb') as tmp:

        if 'xls' in file_name:
            resp = HttpResponse(tmp, content_type='application/vnd.ms-excel;charset=UTF-8')
        else:
            resp = HttpResponse(tmp, content_type='application/text;charset=UTF-8')

        resp['Content-Disposition'] = "attachment; filename=%s" % file_name

    self.logger.debug('Downloading file')

    return resp
