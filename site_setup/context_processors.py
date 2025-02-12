from site_setup.models import SiteSetup

def context_processor_example(request):
    return {
        'example': 'Veio do Context Processor'
    }

def site_setup_meu(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup_meu': setup,
    }