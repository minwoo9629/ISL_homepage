from django.contrib import admin
from django.urls import path, include
from mainapp.views import home
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views
import boardapp.views
import loginapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.home, name="home"),
    path('board/', boardapp.views.board, name="board"),
    path('write', boardapp.views.write, name="write"),
    path('create', boardapp.views.create, name="create"),
    path('dataroom/<int:board_id>/',boardapp.views.detail,name="detail"),
    path('edit/<int:board_id>/',boardapp.views.edit,name="edit"),
    path('delete/<int:board_id>/',boardapp.views.delete,name="delete"),
    path('sign_up',loginapp.views.sign_up,name="sign_up"),
    path('sign_up/<id>', loginapp.views.sign_up, name='sign_up'),
    path('sign_in',loginapp.views.sign_in,name="sign_in"),
    path('logout',loginapp.views.logout, name="logout"),
    path('dataroom/', boardapp.views.dataroom, name="dataroom"),
    path('download/<int:pk>', boardapp.views.file_download, name="file_download"),
    path('search/', boardapp.views.search, name="search"),
    path('id_check', loginapp.views.id_check, name="id_check")
    # path('accounts/',include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
