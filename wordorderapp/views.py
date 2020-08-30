from django.views import generic
from django.contrib.auth import authenticate
from .models import Workorder
from .models import Dailyjournal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.urls import reverse
from django.views.generic import TemplateView


class HomePage1View(TemplateView):

    template_name = 'wordorderapp/homepage1.html'

class IndexView(generic.ListView):
    template_name = 'wordorderapp/index.html'
    paginate_by = 20
    def get_queryset(self):
        return Workorder.objects.filter(user=self.request.user)

    context_object_name = 'index'

class IndexView1(generic.ListView):
    template_name = 'wordorderapp/index1.html'
    paginate_by = 20
    def get_queryset(self):
        return Workorder.objects.all()

    context_object_name = 'index1'

class IndexView2(generic.ListView):
    template_name = 'wordorderapp/index2.html'
    paginate_by = 20
    def get_queryset(self):
        return Workorder.objects.all()

    context_object_name = 'index2'

class DetailView(generic.DetailView):
    model = Workorder
    context_object_name = 'detail'
    template_name = 'wordorderapp/detail.html'

class WorkCreate(CreateView):
    model = Workorder
    fields = ['addressnumber', 'addressstreet', 'addresstown', 'addressstate', 'quickdescrip', 'lockboxcode', 'description', 'proposalorestimatenumber', 'clientemailinfo', 'techniciancompletionnotes', 'taskdatecomplete', 'taskdatestart', 'taskcomplete', 'user', 'invoicesent', 'client']

class WorkUpdate(UpdateView):
    model = Workorder
    fields = ['techniciancompletionnotes', 'taskdatecomplete', 'taskdatestart', 'taskcomplete']
    template_name = 'wordorderapp/workorder_update_form.html'

class WorkUpdate1(UpdateView):
    model = Workorder
    fields = ['invoicesent']
    template_name = 'wordorderapp/workorder_update_form1.html'

class WorkUpdateAdmin(UpdateView):
    model = Workorder
    fields = ['addressnumber', 'addressstreet', 'addresstown', 'addressstate', 'quickdescrip', 'lockboxcode', 'description', 'proposalorestimatenumber', 'clientemailinfo', 'techniciancompletionnotes', 'taskdatecomplete', 'taskdatestart', 'taskcomplete', 'user', 'invoicesent', 'client']
    template_name = 'wordorderapp/workorder_update_formadmin.html'

class WorkDelete(DeleteView):
    model = Workorder
    success_url = reverse_lazy('wordorderapp:index')


class DailyCreate(CreateView):
    model = Dailyjournal
    fields = ['user', 'journaldate', 'description']



class UserFormView(View):
    form_class = UserForm
    template_name = 'wordorderapp/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)


            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User Objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    auth_login(request, user)
                    return redirect('wordorderapp:loginsuccess')

        return render(request, self.template_name, {'form': form})

class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = 'wordorderapp:loginsuccess'
    form_class = AuthenticationForm
    template_name = 'wordorderapp/login_form.html'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=self.request.get_host()):
            redirect_to = reverse(self.success_url)
        return redirect_to

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('wordorderapp:logoutsuccess')
        # return super(LogoutView, self).get(request, *args, **kwargs)

class WorkOrderSearchView(generic.ListView):
    template_name = 'workorder_list.html'
    model = Workorder

    def get_queryset(self):
        try:
            addressstreet = self.kwargs['addressstreet']
        except:
            addressstreet = ''
        if (addressstreet != ''):
            object_list = self.model.objects.filter(addressstreet__icontains = addressstreet)
        else:
            object_list = self.model.objects.all()
        return object_list

class LoginSuccessView(TemplateView):

    template_name = 'wordorderapp/successpage.html'

class LogoutSuccessView(TemplateView):

    template_name = 'wordorderapp/logoutsuccesspage.html'
