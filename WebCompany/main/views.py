from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users
from .models import Department
from .models import Position_Empl, Tokens
from django.views.generic import UpdateView, DeleteView
from dateutil.relativedelta import relativedelta
from datetime import datetime
import uuid
import hashlib

# def Is_Auth(request, id):
#     show = request.COOKIES['usertoken']
#
#     if not show:
#         return False
#
#     return Tokens.objects.get(token=show).id_user.id == id

def Get_Current(request):
    show = request.COOKIES.get('usertoken')

    if not show:
        return None
    return Tokens.objects.get(token=show).id_user

def Custom_Redirect (request, user):

    if Users.objects.get(id=user.id).id_position.name_position == "Сотрудник":
        http = redirect(employee)

    else:
        http = redirect(supervision)

    return http

def login (request):

    if request.method == 'POST':
        log = request.POST.get("log", "Undefined")
        password = request.POST.get("pass", "")

        hash_pass = password.encode()
        hash_pass = hashlib.sha3_256(hash_pass).hexdigest()

        if log != "Undefined":
            user = Users.objects.get(login=log)

            if user:
                if user.password == hash_pass:
                    http = Custom_Redirect(request, user)

                    uu = uuid.uuid1()

                    Tokens.objects.create(token=uu, id_user=user)

                    http.set_cookie('usertoken', uu)

                    return http

    return render(request, 'main/login.html')

def employee (request):

    user = Get_Current(request)

    if not user:
        return redirect(login)

    users = Users.objects.all

    year = relativedelta(datetime.now(),user.date_enter_company).years

    data ={

        'user':user,
        'users': users,
        'year':year,
    }

    return render(request, 'main/employee.html', data)

def logout (request):
    show = request.COOKIES.get('usertoken')

    if Tokens.objects.get(token=show):
        Tokens.objects.get(token=show).delete()

    http = redirect(login)

    http.delete_cookie('usertoken')

    return http

# class UserUpdates(UpdateView):
#     model = Users
#     template_name = 'main/userupdate.html'
#     form_class = UsersForm

def UserUpdates(request):
    back_url = request.META.get('HTTP_REFERER')
    user = Get_Current(request)

    if not user:
        return redirect(login)

    if request.method == 'POST':

        mail = request.POST.get("mail", "Undefined")
        number = request.POST.get("number", "Undefined")

        if mail != "Undefined" and number != "Undefined":
                user.mail = mail
                user.number_phone = number
                user.save()

                http = Custom_Redirect(request, user)

                return http

    data = {
        'user': user,
        'back_url': back_url,
    }

    return render(request, 'main/userupdate.html', data)

def EditPassword(request):
    back_url = request.META.get('HTTP_REFERER')
    user = Get_Current(request)

    if not user:
        return redirect(login)

    error = ""

    if request.method == 'POST':

        newpass = request.POST.get("newpass", "Undefined")
        confirmpass = request.POST.get("confirmpass", "Undefined")
        oldpass = request.POST.get("oldpass", "Undefined")

        hash_newpass = newpass.encode()
        hash_newpass = hashlib.sha3_256(hash_newpass).hexdigest()

        hash_oldpass = oldpass.encode()
        hash_oldpassq = hashlib.sha3_256(hash_oldpass).hexdigest()

        if newpass == "Undefined" or confirmpass == "Undefined" or oldpass == "Undefined":
            error = "Поле или поля не заполнены !"
        elif newpass == confirmpass and hash_oldpassq == user.password:
                user.password = hash_newpass
                user.save()

                http = Custom_Redirect(request, user)

                return http
        else :
            error = "Пароли не совпадают !"
    data = {
        'error': error,
        'back_url': back_url,
    }

    return render(request, 'main/editpassword.html', data)

def EditUser(request, pk):

    back_url = request.META.get('HTTP_REFERER')
    user = Get_Current(request)

    if not user:
        return redirect(login)
    if user.id_position.name_position != "Руководитель":
        return redirect(employee)

    edit_user = Users.objects.get(id=pk)

    if request.method == 'POST':
        sal = request.POST.get("salary", "Undefined")

        if sal != "Undefined":
            edit_user.salary = sal
            edit_user.save()
            redirect(supervision)

    data = {
        'user': user,
        'edituser': edit_user,
        'back_url': back_url,
    }

    return render(request, 'main/edituser.html', data)

def viewprofile (request, pk):

    back_url = request.META.get('HTTP_REFERER')
    user = Get_Current(request)

    if not user:
        return redirect(login)

    view_user = Users.objects.get(id=pk)

    year = relativedelta(datetime.now(), view_user.date_enter_company).years

    data = {
        'user': user,
        'view_user': view_user,
        'back_url': back_url,
        'year': year,
    }

    return render(request, 'main/viewprofile.html', data)


def supervision (request):
    user = Get_Current(request)

    if not user:
        return redirect(login)

    users = Users.objects.all

    year = relativedelta(datetime.now(), user.date_enter_company).years

    data = {

        'user': user,
        'users': users,
        'year': year,
    }

    return render(request, 'main/supervisor.html', data)