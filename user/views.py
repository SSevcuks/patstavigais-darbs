from django.shortcuts import render, HttpResponse
from django.views.generic import View, ListView, FormView, DetailView
from user.models import User
from user.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'users_list.html'


class AddUserView(FormView):
    form_class = UserForm
    template_name = 'form.html'


    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']

        return HttpResponse(f"<p>Username: <strong>{username}"
                            f"</strong><br><br>E-mail: {email}</p>")


class GetUserView(DetailView):
    model = User
    template_name = 'user.html'


class DeleteUserView(View):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        user.delete()

        return HttpResponse(f'Deleted <strong>{user.username}</strong>')


class EditUserView(View):


    def get(self, request, user_id):

        user = User.objects.get(id=user_id)

        context = {
            'user': user,
        }
        return render(
            template_name='edit.html',
            request=request,
            context=context,
        )

    def post(self, request, user_id):

        user = User.objects.get(id=user_id)

        context = {
            'user': user,
        }
        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        return render(
            template_name='user1.html',
            request=request,
            context=context,
        )


