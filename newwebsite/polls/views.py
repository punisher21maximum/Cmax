# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.http import HttpResponse
#template,auth login
from django.shortcuts import render,redirect
from django.views.generic import View
#from .forms import  UserForm
#generic
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book_model,Owner_model,Etx_model,Novel_model,Ebook_model,Enotes_model,Arduino_model,Calc_model

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
#start files
#file import
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
#user and profile
from django.contrib.auth.forms import UserCreationForm
#user
from .forms import UserRegisterForm, UserUpdateForm, Owner_modelUpdateForm
from django.contrib import messages
#profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#filter
from .filters import SnippetFilter, SnippetFilter2, SnippetFilter3, SnippetFilter4
#payment
from django.views.decorators.csrf import csrf_exempt


@login_required
def owner_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = Owner_modelUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.owner_model)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('polls:owner_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = Owner_modelUpdateForm(instance=request.user.owner_model)

    star_books = Book_model.objects.all()
    context = {
        'u_form': u_form,
        'p_form': p_form, 'star_books' : star_books
    }
    
    return render(request,'polls/profile.html',context)
#register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {username}!')
            return redirect('polls:index')
    else:
        form = UserRegisterForm()
    return render(request, 'polls/register_template.html', {'form': form})

#add owner/user form
class OwnerCreate( CreateView):#LoginRequiredMixin,
	model = Owner_model
	fields =  '__all__'




#star start

def favv(request, pk ):
    a_book = get_object_or_404(Book_model, pk = pk)
    a_book.star = True
    a_book.save()
    return render(request, 'polls/index.html')
def unfavv(request, pk ):
    a_book = get_object_or_404(Book_model, pk = pk)
    a_book.star = False
    a_book.save()
    return render(request, 'polls/index.html')
#star end

'''books'''
#homepage,books
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 3 

    #fields =  ['book_name','book_image','pdf','book_branch','book_sub','book_year','author','edition',
    #'sell_price','rent_price_per_month','rent_price_per_week','star']

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_context_data2(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['filter_1b'] = SnippetFilter_1b(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Book_model.objects.all() 

#book detail form
class DetailView(generic.DetailView):
    model = Book_model
    fields =  ['book_name','book_image','pdf','book_branch','book_sub','book_year','author','edition',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']
    template_name = 'polls/detail.html'

#add book form
class BookCreate(LoginRequiredMixin,CreateView):#LoginRequiredMixin,
    model = Book_model
    fields =  ['book_name','book_image','pdf','book_branch','book_sub','book_year','author','edition',
    'sell_price','rent_price_per_month','rent_price_per_week','star','rent_price_per_day']
    #template_name = polls/book_model_form.html
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate,self).form_valid(form)

#updateform
class BookUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#LoginRequiredMixin,
    model = Book_model
    fields =  ['book_name','book_image','pdf','book_branch','book_sub','book_year','author','edition',
    'sell_price','rent_price_per_month','rent_price_per_week','star','rent_price_per_day']
    #template_name = polls/book_model_form.html
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookUpdate,self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False




class DeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Book_model
    success_url = '/polls/'
    template_name = 'polls/confirm_delete_book.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
    

'''enotes'''
#list display------------------------------------------------------
class EnotesIndexView(generic.ListView):
    template_name = 'polls/enotes_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(EnotesIndexView,self).get_context_data(**kwargs)
        context['filter'] = SnippetFilter3(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Enotes_model.objects.all()
#add form------------------------------------------------------
class EnotesCreate(LoginRequiredMixin,CreateView):#UserPassesTestMixin,
  model = Enotes_model
  fields =  ['enotes_author','enotes_topic','enotes_desc','enotes_unit', 
  'enotes_branch','enotes_sub','enotes_year',
  'enotes_drive_url','enotes_image','enotes_pdf']
  #template_name = model_form.html eg. enotes_form.html
  def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(EnotesCreate,self).form_valid(form)

    
#add form------------------------------------------------------
class EnotesUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#UserPassesTestMixin,
    model = Enotes_model
    fields =  ['enotes_author','enotes_topic','enotes_desc','enotes_unit', 
  'enotes_branch','enotes_sub','enotes_year',
  'enotes_drive_url','enotes_image','enotes_pdf']#template_name = model_form.html eg. enotes_form.html
    def form_valid(self, form):

        form.instance.owner = self.request.user
        return super(EnotesUpdate,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

#detail view------------------------------------------------------
class EnotesDetailView(generic.DetailView):
  model = Enotes_model
  template_name = 'polls/enotes_detail.html'
#delete--------------------------------------------------------
class EnotesDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Enotes_model
    success_url = '/polls/'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

'''ebook'''
#list display------------------------------------------------------
class EbookIndexView(generic.ListView):
    template_name = 'polls/ebook_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(EbookIndexView,self).get_context_data(**kwargs)
        context['filter'] = SnippetFilter4(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
		return Ebook_model.objects.all()
#add form------------------------------------------------------
class EbookCreate(LoginRequiredMixin,CreateView):
    model = Ebook_model
    fields =  ['ebook_name','ebook_author','ebook_branch','ebook_sub','ebook_year',
    'ebook_edition','ebook_drive_url','ebook_image','ebook_pdf']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(EbookCreate,self).form_valid(form)

#add form------------------------------------------------------
class EbookUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Ebook_model
    fields =  ['ebook_name','ebook_image','ebook_pdf','ebook_author','ebook_branch','ebook_sub','ebook_year',
    'ebook_edition','ebook_drive_url']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(EbookUpdate,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
#detail view------------------------------------------------------
class EbookDetailView(generic.DetailView):
	model = Ebook_model
	template_name = 'polls/ebook_detail.html'
#delete
class EbookDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Ebook_model
    success_url = '/polls/'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

'''novel'''
#list display------------------------------------------------------
class NovelIndexView(generic.ListView):
    template_name = 'polls/novel_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(NovelIndexView,self).get_context_data(**kwargs)
        context['filter'] = SnippetFilter2(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
		return Novel_model.objects.all()



    
#add form------------------------------------------------------
class NovelCreate(LoginRequiredMixin,CreateView):
    model = Novel_model
    fields =  ['novel_name','genre','author','edition','novel_image','pages','sell_price',
    'rent_price_per_day','rent_price_per_month','rent_price_per_week']
    #template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NovelCreate,self).form_valid(form)

#add form------------------------------------------------------
class NovelUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Novel_model
    fields =  ['novel_name','genre','author','edition','novel_image','pages','sell_price',
    'rent_price_per_day','rent_price_per_month','rent_price_per_week']
    #template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NovelUpdate,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
#detail view------------------------------------------------------
class NovelDetailView(generic.DetailView):
	model = Novel_model
	template_name = 'polls/novel_detail.html'
#delete----------------------------------
class NovelDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Novel_model
    success_url = '/polls/'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

'''etx'''
#etx list display------------------------------------------------------
class EtxIndexView(generic.ListView):
    template_name = 'polls/etx_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 9
    def get_queryset(self):
		return Etx_model.objects.all()
#add etx form------------------------------------------------------
class EtxCreate(LoginRequiredMixin,CreateView):
    model = Etx_model
    fields =  ['item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(EtxCreate,self).form_valid(form)
#update etx form------------------------------------------------------
class EtxUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Etx_model
    fields =  ['item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(EtxUpdate,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
#etx detail view------------------------------------------------------
class EtxDetailView(generic.DetailView):
	model = Etx_model
	template_name = 'polls/etx_detail.html'

#delete-------------------------
class EtxDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Etx_model
    success_url = '/polls/etx/etx_index'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

'''etx_arduino'''
#etx_arduino list display------------------------------------------------------
class Etx_arduino_IndexView(generic.ListView):
    template_name = 'polls/etx_folder/etx_arduino_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 9
    def get_queryset(self):
        return Arduino_model.objects.all()
#etx_arduino detail view------------------------------------------------------
class Etx_arduino_DetailView(generic.DetailView):
    model = Arduino_model
    template_name = 'polls/etx_folder/etx_arduino_detail.html'
#add etx_arduino form------------------------------------------------------
class Etx_arduino_Create(LoginRequiredMixin,CreateView):
    model = Arduino_model
    template_name = 'polls/etx_folder/etx_arduino_model_form.html'
    fields =  ['type_A','cable','jumper_wires','jumper_qty',
    'item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Etx_arduino_Create,self).form_valid(form)

#update etx_arduino form------------------------------------------------------
class Etx_arduino_Update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Arduino_model
    template_name = 'polls/etx_folder/etx_arduino_model_form.html'
    fields = ['type_A','cable','jumper_wires','jumper_qty',
    'item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Etx_arduino_Update,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


#delete-------------------------
class Etx_arduino_DeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Arduino_model
    success_url = '/polls/etx/etx_index'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
 






'''etx calc'''
#etx calc list display------------------------------------------------------
class Etx_calc_IndexView(generic.ListView):
    template_name = 'polls/etx_folder/etx_calc_index.html'
    context_object_name = 'latest_owner_list'
    paginate_by = 9
    def get_queryset(self):
        return Calc_model.objects.all()
#etx calc detail view------------------------------------------------------
class Etx_calc_DetailView(generic.DetailView):
    model = Calc_model
    template_name = 'polls/etx_folder/etx_calc_detail.html'
#add etx calc form------------------------------------------------------
class Etx_calc_Create(LoginRequiredMixin,CreateView):
    model = Calc_model
    template_name = 'polls/etx_folder/etx_calc_model_form.html'
    fields =  ['type_A','desc', 
    'item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Etx_calc_Create,self).form_valid(form)

#update etx calc form------------------------------------------------------
class Etx_calc_Update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Calc_model
    template_name = 'polls/etx_folder/etx_calc_model_form.html'
    fields = ['type_A','desc', 
    'item_image','item_image2','item_image3',
    'sell_price','rent_price_per_month','rent_price_per_week','rent_price_per_day']#template_name = model_form.html eg. novel_form.html
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Etx_calc_Update,self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


#delete-------------------------
class Etx_calc_DeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Calc_model
    success_url = '/polls/etx/etx_index'
    template_name = 'polls/confirm_delete_book.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
 

 



















#upload
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
#end files


'''
def index(request):	
	latest_question_list = Question.objects.order_by('-pub_date')[:5] 
	latest_owner_list = Owner.objects.all()
	context = {	
	'latest_owner_list' : latest_owner_list ,'latest_question_list': latest_question_list
	}
	return render(request, 'polls/index.html', context)

def index(request):
	
	latest_book_list = Book.objects.all()
	context = {	
	'latest_book_list' : latest_book_list 
	}
	return render(request, 'polls/index.html', context)


# Leave the rest of the views (detail, results, vote) unchanged
#tu3

from django.shortcuts import get_object_or_404, render

#from .models import Question,Owner
# ...

def detail(request, question_id):
   
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})#

def detail(request, book_id):  
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'polls/detail.html', {'book':book})#
'''



'''
#forms view
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request,owner_form):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

#endform view
#logsin view
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .logsin import LogsinForm

def log(request,logsin_form):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogsinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogsinForm()

    return render(request, 'polls/logsin.html', {'form': form})
#endform view

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#start book form view
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .bookform import fun_book_form   #func from .py file with form.fields

def get_book_details(request,book_form):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = fun_book_form(request.POST)#func
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = fun_book_form()

    return render(request, 'polls/book_form.html', {'form': form})
'''
#end book form view
#start fav
'''
def favourite(request, album_id):
	album=get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except ( KeyError, Song.DoesNotExist):
		return render(request,'music/detail.html', {
			'album':album,
			'error_message':"you did not select a song",
		})
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album':album})
#end fav

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'polls/results.html', {'question': question,'owner':owner})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''



