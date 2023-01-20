from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def clock(request):
    import requests
    import pytz
    from datetime import datetime
    search = request.POST.get('search')
    if search is not None:
        search = request.POST.get('search').title()
    requests = requests.get("http://api.timezonedb.com/v2.1/list-time-zone?key=MN1YQ966ZTXX&format=json")
    data = requests.json()
    new_data = data["zones"]
    for i in new_data:
        for key, val in i.items():
            if val == search:
                zone = i['zoneName']
                hrs_24 = datetime.now(pytz.timezone(i['zoneName'])).strftime("%H:%M:%S")
                hrs_12 = datetime.now(pytz.timezone(i['zoneName'])).strftime("%I:%M %p")
    try:
        zone, hrs_24, hrs_12
    except NameError:
        zone = None
        hrs_24 = None
        hrs_12 = None
        search = None

    if zone is None:
        zone = ''
        hrs_24 = ''
        hrs_12 = ''
        search = ''
    return render(request, 'index.html', {"zone": zone, "hrs_24": hrs_24, "hrs_12": hrs_12, "search": search})
