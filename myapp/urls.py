from django.urls import Path
from . import views

urlpatterns  = [
    Path('',views,home),
    Path('project/',views,project), 
    Path('about/',views,about),
    Path('contact/',views,contact),
    Path('hire/',views,hire),

]