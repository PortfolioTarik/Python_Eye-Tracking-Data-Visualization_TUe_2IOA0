# Generated and coded by Tarik Hacialiogullari
"""eye_tracking_visualizations_group23a URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Coded by Tarik Hacialiogullari
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('color/', include('color_comparison.urls')),
    path('user/', include('user_comparison.urls')),
    path('manual/', include('manual_comparison.urls')),
    path('import/', include('import_csv.urls')),
    path('heatmap/', include('visualization_heatmap.urls')),
    path('linechart/', include('visualization_linechart.urls')),
    path('barchart/', include('visualization_barchart.urls')),
    path('gazeplot/', include('visualization_gazeplot.urls')),
    path('synchronized/', include('visualization_synchronized.urls')),
]
