from django.conf.urls import url
from .views import  ApiPlayerListView, TeamPlayerList


urlpatterns = [
   
    
    url(r'^team$', TeamPlayerList.as_view({'post': 'list'})),
    url(r'^players$', ApiPlayerListView.as_view())
]