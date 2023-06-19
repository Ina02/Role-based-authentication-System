from django.views.generic.list import ListView

from django.contrib.auth.mixes import LoginRequiredMixin

class SecretView(loginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"