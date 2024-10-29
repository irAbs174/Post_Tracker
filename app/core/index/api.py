from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tools import (
    driver_functions,
    tracking_post
)


@csrf_exempt
def test(request):
    success = False
    # Test Request => curl -d "tracking_code=SIMPLE_CODE" -X POST HOST:PORT
    if request.method == "POST":
        try:
            tracking_code = request.POST.get('tracking_code')
            result = tracking_post.Tracker(tracking_code).run()
            status = 200
            success = True
            
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