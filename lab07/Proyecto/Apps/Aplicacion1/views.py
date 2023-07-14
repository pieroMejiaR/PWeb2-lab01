from django.http import HttpResponse
from django.views.generic import View
from django.template import engines, loader
from .models import render_to_pdf

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template_engine = engines['django']
        template = template_engine.get_template('invoice.html')

        context = {
            "invoice_id": 123,
            "customer_name": "Jhon Cooper",
            "amount": 1399.99,
            "today": "Today"
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(html)
