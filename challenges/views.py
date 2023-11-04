from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

dict_monthly_challenges = {
    "january": "Walk for 20 mins",
    "february": "Walk for 30 mins",
    "march": "Walk for 40 mins",
    "april": "Walk for 50 mins",
    "may": "Walk for 60 mins",
    "june": "Walk for 70 mins",
    "july": "Walk for 80 mins",
    "august": "Walk for 90 mins",   
    "september": "Walk for 100 mins",
    "october": "Walk for 110 mins",
    "november": "Walk for 120 mins",
    "december": "Walk for 130 mins"
}

def index(request):
    month_keys = list(dict_monthly_challenges.keys())
    # list_keys = ""
    # for month in month_keys:
    #     month_path = reverse("month-name", args=[month])
    #     list_keys = list_keys + f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    # response_data = f"<ul><h1>{list_keys}</h1></ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {"month_keys": month_keys})



def month_by_number(request, id):
    month_keys = list(dict_monthly_challenges.keys())
    if id > len(month_keys):
        return HttpResponseNotFound("Could not find monthly challenge")
    month_redirect = month_keys[id - 1] # -1 to make index 0 as January
    # redirect_path = reverse("month-name", args=[month_redirect])
    # return HttpResponseRedirect(redirect_path)
    return HttpResponseRedirect("/challenges/" + month_redirect)


def month(request, id):
    try:
        challenged_test = dict_monthly_challenges[id]
        # response_data = f"<h1>{challenged_test}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request,"challenges/challenge.html",{"text": challenged_test, "month": id})
    except:
        raise Http404()
        # resp = render_to_string('404.html')
        # return HttpResponse(resp)
        # return HttpResponseNotFound("<h1>Could not find monthly challenge<h1>")



