from .models import Sponsor

def sponsors(request):
    sponsors = Sponsor.objects.all()
    return {'sponsors': sponsors}