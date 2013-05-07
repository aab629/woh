from woh.data.models import Woh
from django.shortcuts import render_to_response


# Remember: Django views are simply functions that accept a HTTP request as an argument
def index(request):
    # First we're going to get a list of all the crimes in our dataset
    all_viols = Woh.objects.all().order_by('-case_violtn_cnt')

    # If we wanted to get crimes of a certain type, we could employ Django's filtering functionality.
    # Say we wanted all the crimes of type 'TRAFFIC'. That might look like this:
    # traffic_crimes = Crime.objects.filter(type='TRAFFIC')

    # Either way, now we're going to send them to a template using Django's render_to_response shortcut
    return render_to_response('index.html', {'incidents': all_viols})


def biz_detail(request, biz_nm):
    
    # In this example, we're going to get a single crime from the database
    biz = Woh.objects.get(id=biz_nm)

    # ... and we'll send it to a different template in exactly the same way as above
    return render_to_response('biz_detail.html', {'biz': biz})

def overtime(request):
    overtime = Woh.objects.all().order_by('-flsa_ot_bw_atp_amt')
    return render_to_response('overtime.html', {'overtime': overtime})
