from tools.driver_functions import DriverFunctions as DF
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from core.SEC import tracking_url as portal
from .tracker_forms import ScreenShotForm
from .tracker_models import ScreenShot
from django.http import JsonResponse

@csrf_exempt
def store_tracking_screenshot(request):
    success = False
    # Test Request => curl -d "tracking_code=SIMPLE_CODE" -X POST HOST:PORT
    if request.method == "POST":
        try:
            # Send tracking variables as arg => tools dir
            tracking_code = request.POST.get('tracking_code')
            # Prepare required PNG image screen shot
            res = DF(portal, tracking_code).run()
            screen_shot = ContentFile(res['img'], name=f"{tracking_code}.png")
            
            # Define variable form_data for sort returned data
            form_data = {
                'orders_number': None,
                'tracking_number': tracking_code,
                'phone_number': None,
                'customer': None,
            }
            
            # Initialize the form with the data
            form = ScreenShotForm(data=form_data)
            
            # Store returned data with django form
            screenshot_instance = form.save(commit=False)
            screenshot_instance.image.save(f"{tracking_code}.png", screen_shot)
            screenshot_instance.save()
            
            """ Prepare json response dara include: 
                status as (int), result as(dict) & success as(bol)
                variables for return """
            
            status = 200
            success = True
            result = {
                'tracking_code': screenshot_instance.tracking_number,
                'img': screenshot_instance.image.url
            }
            
        except Exception as error:
            print(f"ERROR +>>>\n{error}")
            result = "Internal server error"
            status = 503
    else:
        result = "Forbidden: not allowed method"
        status = 403
    return JsonResponse({
        'status':status,
        'result': result,
        'success': success
    })