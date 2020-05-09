from django.shortcuts import render

# Create your views here.


def home(request):
    # here include all graphs from import and show them

    # show the results
    script = ''
    div = '<h1>Line chart</h1><br><h1>Bar chart</h1><br><h1>Heatmap</h1><br><h1>Gaze plot</h1>'
    #script, div = components(row(p1,p2,p3,p4))
    return render(request, 'website_synchronized.html',
                  {'script': script, 'div': div})
