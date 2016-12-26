import django_tables2 as tables
from django_tables2.utils import A
from voiper.models import Number
import itertools


class NumberTable(tables.Table):
    # number = tables.Column(
    #     verbose_name='Numer',
    #     attrs={'th': {'id': 'foo'}},
    # )
    number = tables.LinkColumn(
        'voip_number:edit',
        verbose_name='Numer',
        args=[A('pk')],
        # args=[Number('pk')]
    )
    customer = tables.Column(
        verbose_name='Klient',
        accessor='id_customer.name'
    )
    context = tables.LinkColumn(
        'voip_context:edit',
        verbose_name='Kontekst',
        accessor='id_context.name',
        args=[A('pk')],
    )
    table_pagination = {
        'per_page': 10
    }

    def __init__(self, *args, **kwargs):
        super(NumberTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return 'Row %d' % next(self.counter)

    class Meta:
        model = Number
        # add class="paleblue" to <table> tag
        sequence = (
            'number',
            'customer',
            'context',
            'secretary',
            'secretary_number',
        )
        fields = (
            'number',
            'secretary',
            'secretary_number',
        )
        attrs = {'class': 'impresario'}
