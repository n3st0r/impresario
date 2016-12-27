from django.views.generic import ListView, DetailView, View

from impresario.models import Customer
from voiper.models import Number
from voiper.services.dialplan import create_sip_accounts


class CustomersView(ListView):
    template_name = 'sip/list.html'
    model = Customer
    # queryset = Contract.objects.all().select_related('id_number__id_customer')
    queryset = Customer.objects.all()


class CustomerSipView(DetailView):
    template_name = 'sip/view.html'
    model = Customer
    context_object_name = 'customer'
    # queryset = Number.objects.filter(id_customer=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CustomerSipView, self).get_context_data(**kwargs)
        context['numbers'] = Number.objects.filter(id_customer=context['customer'].pk)
        context['config'] = create_sip_accounts(context['numbers'])

        return context
