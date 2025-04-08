from django.contrib import messages
from userauths.models import User, CustomerAddress
from userauths.forms import updateUserForm, updatePasswordForm, customerAddress


def processor(request):
    user_instance = User.objects.get(username=request.user.username)

    if request.method == "POST":
        userform = updateUserForm(request.POST, instance=user_instance)
        if userform.is_valid():
            userform.save()
            messages.success(request, "Profile updated successfully!!")
    else:
        userform = updateUserForm(instance=user_instance)

    passwordform = updatePasswordForm(user=request.user)

    return {
        'userform': userform,
        'passwordform': passwordform,
        'addresses': CustomerAddress.objects.filter(user_id=request.user.id),
        'addressform': customerAddress()
    }
