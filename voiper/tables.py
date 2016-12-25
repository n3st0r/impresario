import django_tables2 as tables
from voiper.models import Context


class ContextTable(tables.Table):
    class Meta:
        model = Context
        # add class="paleblue" to <table> tag
        attrs = {'class': 'impresario'}
