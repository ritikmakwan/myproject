from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('showstudents',views.showstudents,name='showstudents'),
    path('updatestudent',views.updatestudent,name='updatestudent'),
    path('searchstudent',views.searchstudent,name='searchstudent'),
    path('joinstudent',views.joinstudent,name='joinstudent'),
    path('showjoinstudent',views.showjoinstudent,name='showjoinstudent'),
    path('updatejoinstudent',views.updatejoinstudent,name="updatejoinstudent"),
    path('searchjoinedstudent',views.searchjoinedstudent,name="searchjoinedstudent"),
    path('batch',views.batch,name="batch"),
    path('trainer',views.trainer,name="trainer")
]
