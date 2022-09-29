from django.http import HttpResponse
from django.shortcuts import redirect

"""
This will hold the access privileges for the Users and Admin so that they
cannot access each othersdata. It will also prevent the user that is already
logged in from seeing/accessing the register or login page.
"""


def unauthorised_person(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        return wrapper_func


def authenticated_users(allowed_roles=[]):
    def decorator(view_func): 
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("<h1>Error! You do not have access to this"  /
                "page,please return to home page.</h1>")
        return wrapper_func
    return decorator
