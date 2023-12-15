from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from .views import tr_handler404
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
]

handler401 = 'app.views.tr_handler401'
handler403 = 'app.views.tr_handler403'
handler404 = 'app.views.tr_handler404'
handler500 = 'app.views.tr_handler500'

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
    path('staff/', include('staff.urls')),
    path('news/', include('news.urls')),
    path('specs/',include('specialties.urls')),
    path('worldskills/',include('worldskills.urls')),
    path('', include('state.urls')),
    path('', include('educational_work.urls')),
    # prefix_default_language=False,
)

# urlpatterns += i18n_patterns(
#     path('', include('main.urls')),
#     path('staff/', include('staff.urls')),
#     path('news/', include('news.urls')),
#     path('worldskills/',include('worldskills.urls')),
#     path('specs/',include('specialties.urls')),
#     path('', include('state.urls')),
# )

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)