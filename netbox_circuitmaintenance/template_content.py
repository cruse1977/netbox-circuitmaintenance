from netbox.plugins import PluginTemplateExtension
from django.db.models import Q
from .models import CircuitMaintenanceImpact 

class CircuitMaintenanceList(PluginTemplateExtension):
    model = 'circuits.circuit'

    def full_width_page(self):

        return self.render('netbox_circuitmaintenance/circuitmaintenance_include.html', extra_context={
            'circuitmaintenance': CircuitMaintenanceImpact.objects.filter(circuit__cid=self.context['object'].cid, circuitmaintenance__status__in=['TENTATIVE', 'CONFIRMED', 'IN-PROCESS', 'RESCHEDULED', 'UNKNOWN']),
        })

class ProviderMaintenanceList(PluginTemplateExtension):
    model = 'circuits.provider'

    def full_width_page(self):

        return self.render('netbox_circuitmaintenance/providermaintenance_include.html', extra_context={
            'circuitmaintenance': CircuitMaintenanceImpact.objects.filter(circuitmaintenance__provider=self.context['object'], circuitmaintenance__status__in=['TENTATIVE', 'CONFIRMED', 'IN-PROCESS', 'RESCHEDULED', 'UNKNOWN']),
        })

class SiteMaintenanceList(PluginTemplateExtension):
    model = 'dcim.site'

    def full_width_page(self):

        return self.render('netbox_circuitmaintenance/providermaintenance_include.html', extra_context={
            'circuitmaintenance': CircuitMaintenanceImpact.objects.filter(Q(circuit__termination_a__site=self.context['object']) | Q(circuit__termination_z__site=self.context['object']), circuitmaintenance__status__in=['TENTATIVE', 'CONFIRMED', 'IN-PROCESS', 'RESCHEDULED', 'UNKNOWN']),
        })


template_extensions = [CircuitMaintenanceList, ProviderMaintenanceList, SiteMaintenanceList]