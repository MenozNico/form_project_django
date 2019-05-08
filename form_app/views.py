from django.http import HttpResponse, request, Http404
from django.shortcuts import render

from .models import Message
from .forms import MessageForm
from django.views.generic.base import TemplateView

# from django.views.generic.edit import ProcessFormView

from .forms import FormContact


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def ContactView(request):
    form_class = MessageForm
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save()
            return render(request, 'contact.html', {'message': new_message.email})
    elif request.method == 'GET':
        return render(request, 'contact.html', {
            'form': form_class,
        })
    else:
        raise Http404