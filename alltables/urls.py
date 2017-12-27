from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.views import password_reset, \
    password_reset_done, password_reset_confirm, password_reset_complete


from . import views
app_name = 'pages'

urlpatterns = [
    # url(r'char$', views.characters, name='characters'),
    # url(r'owls$', views.owls, name='owls'),
    # url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^$', views.account, name='thanks'),
    # url(r'^ups/', views.ups, name='ups'),
    url(r'^letters/$', views.letters, name='letters'),
    # url(r'^1/', views.test, name='test'),
    url(r'^login/$', login, {'template_name':'pages/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name':'pages/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),

    url(r'^password_reset/$', password_reset, {'template_name':
        'pages/password_reset.html', 'post_reset_redirect': 'account:password_reset_done',
        'email_template_name': 'pages/password_reset_email.html'}, name='password_reset'),

    url(r'^password_reset/done/$', password_reset_done, {'template_name':'pages/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {'template_name':
        'pages/password_reset_confirm.html', 'post_reset_redirect': 'account:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^password_reset/complete/$', password_reset_complete, {'template_name':'pages/password_reset_complete.html'},
        name='password_reset_complete'),
]



