import django_filters
from .models import Book_model,Novel_model,Enotes_model,Ebook_model



class SnippetFilter(django_filters.FilterSet):

	'''sell_price'''
	sell_price__gt = django_filters.NumberFilter(label='min', lookup_expr='gt')
	sell_price__lt = django_filters.NumberFilter(label='max', lookup_expr='lt')
	#bookname
	book_name = django_filters.CharFilter(lookup_expr='icontains',label='book name' )
	#author
	author = django_filters.CharFilter(lookup_expr='icontains',label='author')
	#owner
	owner__username = django_filters.CharFilter(lookup_expr='icontains',label='owner')
	###	    
	###
	 
	class Meta:
		model = Book_model
		fields = (

			'book_name',
			'author' ,
			'book_branch',
			'book_sub',
			'book_year',

			
			)

	'''order by price'''
	CHOICES = (
		('asc','Asc'),
		('desc','Desc'),
		)
	ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES,method='filter_by_order')
	
	def filter_by_order(self,queryset,name,value):
			expression = 'sell_price' if value == 'asc' else '-sell_price'
			return queryset.order_by(expression)


class SnippetFilter_1b(django_filters.FilterSet):


	#bookname
	book_name = django_filters.CharFilter(lookup_expr='icontains' )
	#author
	author = django_filters.CharFilter(lookup_expr='icontains')
	
	class Meta:
		model = Book_model
		fields = (

			'book_name',
			'author' ,

			)

class SnippetFilter2(django_filters.FilterSet):

	#sell_price
	sell_price__gt = django_filters.NumberFilter(label='min', lookup_expr='gt')
	sell_price__lt = django_filters.NumberFilter(label='max', lookup_expr='lt')
	#novel_name
	novel_name = django_filters.CharFilter(label='novel name',lookup_expr='icontains')
	#author
	author = django_filters.CharFilter(label='author',lookup_expr='icontains')
	#genre
	#genre = django_filters.CharFilter(lookup_expr='icontains')
	#edition
	edition = django_filters.CharFilter(label='year',lookup_expr='icontains')
	#pages
	pages = django_filters.CharFilter(label='pages less then',lookup_expr='lt')
	#owner
	owner__username = django_filters.CharFilter(lookup_expr='icontains',field_name='owner')
	###	    
	####	
	
	class Meta:
		model = Novel_model
		fields = (

			'novel_name','genre' ,'author','edition', 'pages',		
			
			)

	#order by price
	
	CHOICES = (
		('asc','Asc'),
		('desc','Desc'),
		)
	ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES,method='filter_by_order')
	
	def filter_by_order(self,queryset,name,value):
			expression = 'sell_price' if value == 'asc' else '-sell_price'
			return queryset.order_by(expression)

class SnippetFilter3(django_filters.FilterSet):#enotes
	#enotes_author
	enotes_author = django_filters.CharFilter(label='enotes author',lookup_expr='icontains')
	#enotes_topic
	enotes_topic = django_filters.CharFilter(label='enotes topic',lookup_expr='icontains')
	#enotes_topic
	enotes_desc = django_filters.CharFilter(label='enotes desc',lookup_expr='icontains')
	
	#enotes_date
	enotes_date = django_filters.CharFilter(label='date',lookup_expr='icontains')
	#owner
	owner__username = django_filters.CharFilter(label='owner',lookup_expr='icontains',field_name='owner')
	###	    
	###
	
	class Meta:
		model = Enotes_model
		fields = (

			'enotes_year',
			'enotes_sub' ,
			'enotes_branch',
			'enotes_author',
			'enotes_topic',
			'enotes_desc',
			'enotes_unit',
			'enotes_date',
			
			)

class SnippetFilter4(django_filters.FilterSet):#enotes
	#ebook_name
	ebook_name = django_filters.CharFilter(lookup_expr='icontains',label='ebook name')
	#ebook_author
	ebook_author = django_filters.CharFilter(lookup_expr='icontains',label='author')
	#ebook_edition
	ebook_edition = django_filters.CharFilter(lookup_expr='icontains',label='year')
	#owner
	owner__username = django_filters.CharFilter(lookup_expr='icontains',field_name='owner')
	###	    
	###
	
	class Meta:
		model = Ebook_model
		fields =  [
		'ebook_name',
		'ebook_author',
		'ebook_branch',
		'ebook_sub',
		'ebook_year',
    	'ebook_edition',
    	]
	
	



