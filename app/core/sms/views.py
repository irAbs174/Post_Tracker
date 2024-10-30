from django.views.decorators.csrf import csrf_exempt
from index.report_models import OrderCodes
from django.http import JsonResponse
from django.shortcuts import render
from core.SEC import SMS_API
from kavenegar import *

def index(request):
    return render(request, 'sms.html')

@csrf_exempt
def new_code(request):
    status, response = 503, 'error'
    ''' 
    receive required data from request for store new code to db
    and send sms with phone number to customer 
    '''
    order_code = request.POST.get("order_code")
    full_name = request.POST.get("full_name")
    tracking_code = request.POST.get("tracking_code")
    phone_number = request.POST.get("phone_number")
    # create new data object
    obj = OrderCodes.objects.all().create(
        orders_number = order_code,
        tracking_number = tracking_code,
        phone_number = phone_number,
        customer = full_name
    )
    # Now sms time!
    try:
        api = KavenegarAPI(SMS_API)
        params = {
            'receptor': phone_number,
            'template': 'kif123Report',
            'token': tracking_code,
            'type': 'sms',
        }
        response = api.verify_lookup(params)
        status = 200
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

    return JsonResponse({
        'status' : status,
        'data' : "successfuly stored new code! " if status == 200 else "",
        'success': True if status == 200 else False
    })



