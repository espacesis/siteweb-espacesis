from django.shortcuts import render
from django.views.generic import View

class HomePage(View):
    """
    the class rendering the main page
    """

    template_name    = 'home/homepage.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {}
        )

def handler404(request):
    return render(request,'404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler400(request):
    return render(request, '400.html', status=400)
