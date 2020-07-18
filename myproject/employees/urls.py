from django.conf.urls import url 
from employees import views 
 
urlpatterns = [ 
    url(r'^api/employees$', views.employees_list),
    url(r'^api/employees/(?P<pk>[0-9]+)$', views.employees_detail),
    url(r'^api/tutorials/ispermanent$', views.employees_list_permament)
]