import django_tables2 as tables
from django_tables2.utils import A
from voiper.models import Contract
import itertools


class ContractTable(tables.Table):

    id = tables.LinkColumn(
        'voip_contract:edit',
        verbose_name='Kontrakt nr',
        args=[A('pk')],
    )

    def __init__(self, *args, **kwargs):
        super(ContractTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return 'Row %d' % next(self.counter)

    class Meta:
        model = Contract
        # add class="paleblue" to <table> tag
        attrs = {'class': 'impresario'}
        sequence = (
            'id',
            'id_number',
            'id_device',
            # 'secretary',
            # 'secretary_number',
        )
