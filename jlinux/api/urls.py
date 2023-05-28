from django.urls import path, include

urlpatterns = [
    path('blog/', include(('jlinux.blog.urls', 'blog'))),
    path('users/', include(('jlinux.users.urls', 'users'))),
    path('auth/', include(('jlinux.authentication.urls', 'auth'))),
]
