from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken import views

from python101.views import signin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('tweet.urls')),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', signin)
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]
