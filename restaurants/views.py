from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):


    context = {
    	"my_list": [
    					{
    						"restaurant_name": "MacDonalds",
    						"food_type": "Burger"
    					},
    					{
    						"restaurant_name": "KFC",
    						"food_type": "Fried Chicken"
    					},
    					{
    						"restaurant_name": "Starbucks",
    						"food_type": "Drinks"
    					},
    				]
    		}
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {
    					"restaurant_name": "Starbucks",
    					"food_type": "Drinks"
    				},
    }
    return render(request, 'detail.html', context)
