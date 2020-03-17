from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    login, logout, 
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete,
    PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
)
app_name = 'polls'

urlpatterns = [

#etx
#etx new item form
    url(r'^etx/add/$', views.EtxCreate.as_view(), name='etx_add'),
#etx update item form
    url(r'^etx/(?P<pk>[0-9]+)/update/$', views.EtxUpdate.as_view(), name='etx_update'),
#etx_index display
    url(r'^etx/etx_index$', views.EtxIndexView.as_view(), name='etx_index'),
#etx_detail display
    url(r'^etx/etx_index/(?P<pk>[0-9]+)/$', views.EtxDetailView.as_view(), name='etx_detail'),
#etx delete item form
    url(r'etx/(?P<pk>[0-9]+)/delete/$', views.EtxDeleteView.as_view(), name='etx_delete'),
#endetx

#etx_ardunio
#etx new item form
    url(r'^etx/add_arduino/$', views.Etx_arduino_Create.as_view(), name='etx_arduino_add'),
#etx update item form
    url(r'^etx/(?P<pk>[0-9]+)/update_arduino/$', views.Etx_arduino_Update.as_view(), name='etx_arduino_update'),
#etx_index display
    url(r'^etx/etx_arduino_index$', views.Etx_arduino_IndexView.as_view(), name='etx_arduino_index'),
#etx_detail display
    url(r'^etx/etx_arduino_index/(?P<pk>[0-9]+)/$', views.Etx_arduino_DetailView.as_view(), name='etx_arduino_detail'),
#etx delete item form
    url(r'etx/(?P<pk>[0-9]+)/delete_arduino/$', views.Etx_arduino_DeleteView.as_view(), name='etx_arduino_delete'),
#endetx_ardunio

 #etx_calc
#etx new item form
    url(r'^etx/add_calc/$', views.Etx_calc_Create.as_view(), name='etx_calc_add'),
#etx update item form
    url(r'^etx/(?P<pk>[0-9]+)/update_calc/$', views.Etx_calc_Update.as_view(), name='etx_calc_update'),
#etx_index display
    url(r'^etx/etx_calc_index$', views.Etx_calc_IndexView.as_view(), name='etx_calc_index'),
#etx_detail display
    url(r'^etx/etx_calc_index/(?P<pk>[0-9]+)/$', views.Etx_calc_DetailView.as_view(), name='etx_calc_detail'),
#etx delete item form
    url(r'etx/(?P<pk>[0-9]+)/delete_calc/$', views.Etx_calc_DeleteView.as_view(), name='etx_calc_delete'),
#endetx_calc

#novel
#novel new item form
    url(r'^novel/add/$', views.NovelCreate.as_view(), name='novel_add'),
#novel update item form
    url(r'^novel/(?P<pk>[0-9]+)/update/$', views.NovelUpdate.as_view(), name='novel_update'),
#novel_index display
    url(r'^novel/novel_index$', views.NovelIndexView.as_view(), name='novel_index'),
#novel_detail display
    url(r'^novel/novel_index/(?P<pk>[0-9]+)/$', views.NovelDetailView.as_view(), name='novel_detail'),
#novel delete item form
    url(r'novel/(?P<pk>[0-9]+)/delete/$', views.NovelDeleteView.as_view(), name='novel_delete'),

#novel





#enotes
#enotes new item form
    url(r'^enotes/add/$', views.EnotesCreate.as_view(), name='enotes_add'),
#enotes update item form
    url(r'^enotes/(?P<pk>[0-9]+)/update/$', views.EnotesUpdate.as_view(), name='enotes_update'),
#enotes_index display
    url(r'^enotes/enotes_index$', views.EnotesIndexView.as_view(), name='enotes_index'),
#enotes_detail display
    url(r'^enotes/enotes_index/(?P<pk>[0-9]+)/$', views.EnotesDetailView.as_view(), name='enotes_detail'),
#enotes delete item form
    url(r'enotes/(?P<pk>[0-9]+)/delete/$', views.EnotesDeleteView.as_view(), name='enotes_delete'),
#enotes


#ebook
#ebook new item form
    url(r'^ebook/add/$', views.EbookCreate.as_view(), name='ebook_add'),
#ebook update item form
    url(r'^ebook/(?P<pk>[0-9]+)/update/$', views.EbookUpdate.as_view(), name='ebook_update'),
#ebook_index display
    url(r'^ebook/ebook_index$', views.EbookIndexView.as_view(), name='ebook_index'),
#ebook_detail display
    url(r'^ebook/ebook_index/(?P<pk>[0-9]+)/$', views.EbookDetailView.as_view(), name='ebook_detail'),
#ebook delete item form
    url(r'ebook/(?P<pk>[0-9]+)/delete/$', views.EbookDeleteView.as_view(), name='ebook_delete'),
#ebook

#enggbook
    #book new item form
    url(r'book/add/$', views.BookCreate.as_view(), name='book-add'),
    #book update item form
    url(r'^book/(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    #book delete item form
    url(r'book/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='book_delete'),
    #homepage:book_index display   
    url(r'^$', views.IndexView.as_view(), name='index'),
    #book_detail display
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #book star
    #url(r'^favv/<pk>/$', views.favv, name='favv'),

    url(r'^(?P<pk>[0-9]+)/favv/$', views.favv, name='favv'),

    #book star
    url(r'^(?P<pk>[0-9]+)/unfavv/$', views.unfavv, name='unfavv'),
#endenggbook




#four url: homepage(books),detailview,form new user,form new book
    #create owner
    url(r'owner/add/$', views.OwnerCreate.as_view(), name='owner-add'),
    #profile
    url(r'^profile/$',views.owner_profile, name='owner_profile'),
    #user
    url(r'^register/$', views.register, name='register' ),
    url('^login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='polls/logout.html'),name='logout'),
#endFourUrl



 





#password reset
    url(r'^password_change/$' ,auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$' ,auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    #reset password
    #url(r'^reset-password/$', password_reset, name='password_reset') ,
    #url(r'^reset-password/done/$', password_reset, name='password_reset_done') ,
    #url(r'^reset-password/done/$', password_reset_done, {'template_name': 'polls/reset_password_done.html'}, name='password_reset_done'),
    
    url(r'^password_reset/$',
         PasswordResetView.as_view(),
         name='password_reset')
    ,

    url(r'^password_reset/done/$',
         PasswordResetDoneView.as_view(
             #template_name='polls/password_reset_done.html'
            ),
         name='password_reset_done')
    ,
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',

         PasswordResetConfirmView.as_view(
             template_name='polls/password_reset_confirm.html',
             #set_password_form=SetPasswordForm,
             #post_reset_redirect='users:reset_complete',

            ),
         name='password_reset_confirm')
    ,
    url(r'^reset/done/$',
         PasswordResetCompleteView.as_view(
             #template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete')
    ,

    
]
























'''
#password reset
    url('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='polls/password_reset.html'
         ),
         name='password_reset'),
    url('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='polls/password_reset_done.html'
         ),
         name='password_reset_done'),
    url('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='polls/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),'''
'''
    url(r'^password-reset/$', 
        #password_reset,
        auth_views.PasswordResetView.as_view(template_name='polls/password_reset.html'),
        name='password_reset'),

    url(r'^password-reset/done/$', 
        #password_reset_done,
        auth_views.PasswordResetDoneView.as_view(template_name='polls/password_reset_done.html',
            ),{'post_reset_redirect': 'polls:password_reset_confirm'},
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        #password_reset_confirm,

        auth_views.PasswordResetConfirmView.as_view(template_name='polls/password_reset_confirm.html'),
        name='password_reset_confirm'),
    '''
'''
url(r'book/(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    #book delete item form
    url(r'book/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='book-delete'),
#user
    url(r'^register/$', views.register, name='register' ),
    url('^login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='polls/logout.html'),name='logout'),
#profile
    url(r'^profile/$',views.profile, name='profile'),
#end file upload


#url(r'^(?P<question_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
    # ex: /polls/
    #url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #register

    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #
    #url(r'^(?P<question_id>[0-9]+)/temp/$', views.vote, name='temp'),
    #
    #url(r'^(owner_form)/$', views.get_name, name='get_name'),
    #
    #url(r'^(logsin_form)/$', views.log, name='log'),
    #
    #url(r'^(?P<book_data_form>book_form)/$', views.get_book_details, name='get_book_details'),
'''

