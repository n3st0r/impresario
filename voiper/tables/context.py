import django_tables2 as tables
from voiper.models import Context
import itertools


class ContextTable(tables.Table):

    def __init__(self, *args, **kwargs):
        super(ContextTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return 'Row %d' % next(self.counter)

    class Meta:
        model = Context
        # add class="paleblue" to <table> tag
        attrs = {'class': 'impresario'}
