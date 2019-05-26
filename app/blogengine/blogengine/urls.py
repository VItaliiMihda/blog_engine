from django.contrib import admin
from django.urls import path, include
from .views import redirect_block
from users import views as usersView

urlpatterns = [
    path('', redirect_block),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('registration/', usersView.signup, name="registration"),
    path('logout/', usersView.logout_view, name="logout"),
    path('login/', usersView.login_view, name="login"),
]
