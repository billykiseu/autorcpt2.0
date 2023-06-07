from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

#URL patterns
urlpatterns = [
    #basic nav
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('clean', views.clean, name='clean'),
    path('savetodb/', views.savetodb, name='savetodb'),
    path('edit-records/', views.edit_records, name='edit_records'),
    path('template/', views.template, name='template'),
    path('receipts/', views.receipts, name='receipts'),
    
    #credentials
    path('login', views.loginUser, name="login"),
    path('accounts/login/?next=/dashboard', views.loginUser, name="accounts/login/?next=/dashboard"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('recover', views.recover, name="recover"),
    path('recoverdone', auth_views.PasswordResetDoneView.as_view(
        template_name="recoverdone.html"), name="recoverdone"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="reset.html"), name="password_reset_confirm"),
    path('recovercomplete', auth_views.PasswordResetCompleteView.as_view(
        template_name="recovercomplete.html"), name="password_reset_complete"),
    
    #fails
    path('loginfail', views.loginfail, name="loginfail"),
    path('recoverfail', views.recoverfail, name="recoverfail"),
    path('permission_denied', views.permission_denied, name="permission_denied"),
    
    #Search
    path('search/', views.search, name="search"),
    
    #downloadable files
    path('Manual/', views.manual, name='manual'),
    
    #data executes
    path('generate', views.generate_receipts, name='generate'),
    path('sendmail', views.send_receipts, name='send_mail'),
    path('quofile', views.generate_excel, name='quofile'),
    path('quoupdate', views.update_excel, name='quoupdate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

