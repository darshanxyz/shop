from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import Item, Category
from .forms import ItemForm
from django.views.decorators.csrf import csrf_exempt

def items(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    search_query = request.GET.get("search_query")
    if search_query:
    	items = items.filter(title__icontains=search_query)
    context = {
    	"items": items,
    	"categories": categories
    }
    return render(request, 'items.html', context)
	
def add(request):
	form = ItemForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form_instance = form.save(commit = False)
		form_instance.save()
		return HttpResponseRedirect(form_instance.get_absolute_url())

	context = {
		'form': form
	}
	if request.user.is_authenticated():
		return render(request, 'add_item.html', context)
	else:
		return render(request, 'items.html', context)

def remove(request, id):
	item = get_object_or_404(Item, id = id)
	item.delete()
	return redirect('items:items')

def item_detail(request, id):
	item = get_object_or_404(Item, id=id)
	items = Item.objects.all()
	search_query = request.GET.get("search_query")
	if search_query:
		items = items.filter(title__icontains=search_query)
		context = {
			"items": items
		}
		return render(request, 'items.html', context)
	rating = item.rating
	context = {
		'item': item,
		'title': item.title,
	}
	return render(request, 'item_detail.html', context)

def update_rating(request):
	if request.method == 'POST':
		item_id = request.POST['item_id']
		if 'rating' in request.POST:
			rating = request.POST['rating']
			items = Item.objects.all()
			for item in items:
				if item.id == int(item_id):
					if request.user in item.rated.all():
						return redirect('items:item_detail')
					if item.number_of_ratings == 0:
						obj = Item.objects.get(id=int(item_id))
						obj.rating = int(rating)
						obj.number_of_ratings += 1
						obj.sum_of_ratings += int(rating)
						obj.rated.add(request.user)
						obj.save()
					else:
						obj = Item.objects.get(id=int(item_id))
						obj.number_of_ratings += 1
						obj.sum_of_ratings += int(rating)
						avg_rating = obj.sum_of_ratings/float(obj.number_of_ratings)
						round(avg_rating, 1)
						obj.rating = avg_rating
						obj.rated.add(request.user)
						obj.save()
			return render(request, 'item_rating.html', {'rating': rating})

def buy(request, id):
	item = get_object_or_404(Item, id=id)
	item.users.add(request.user)
	context = {
		'user': request.user,
		'item': item,
		'title': item.title,
	}
	return render(request, 'item_detail.html', context)