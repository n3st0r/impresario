from django.views.generic import ListView, DetailView, CreateView
from django.http import JsonResponse
from django.template.loader import render_to_string

from impresario.models import Customer
from voiper.models import Number, Stencil
from voiper.services.dialplan import create_sip_accounts, create_incoming_dialplan
from voiper.forms import StencilForm


class CustomersView(ListView):
    template_name = 'asterisk/list.html'
    model = Customer
    # queryset = Contract.objects.all().select_related('id_number__id_customer')
    queryset = Customer.objects.all()


class StencilView(ListView):
    template_name = 'asterisk/stencil_list.html'
    model = Stencil
    # queryset = Contract.objects.all().select_related('id_number__id_customer')
    queryset = Stencil.objects.all()


def stencil_create(request):
    data = dict()

    if request.method == 'POST':
        form = StencilForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = StencilForm()

    context = {'form': form}
    data['html_form'] = render_to_string(
        'asterisk/partial_stencil_add.html',
        context,
        request=request
    )
    return JsonResponse(data)


class CustomerSipView(DetailView):
    template_name = 'asterisk/view.html'
    model = Customer
    context_object_name = 'customer'
    # queryset = Number.objects.filter(id_customer=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CustomerSipView, self).get_context_data(**kwargs)
        context['numbers'] = Number.objects.filter(id_customer=context['customer'].pk)
        context['config'] = create_sip_accounts(context['numbers'])
        context['dialplan'] = create_incoming_dialplan(context['numbers'])

        return context
