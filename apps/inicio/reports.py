
from model_report.report import reports, ReportAdmin
from apps.producto.models import Marca

class AnyModelReport(ReportAdmin):
 
    model = Marca
    fields = [
        'nombre',
    ]
    list_order_by = ('nombre',)
    type = 'report'

reports.register('anymodel-report', AnyModelReport)