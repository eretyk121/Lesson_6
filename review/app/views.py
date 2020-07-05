from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm




def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


# def product_view(request, pk):
#     template = 'app/product_detail.html'
#     product = get_object_or_404(Product, id=pk)
#     reviews = Review.objects.all()
#     if request.method == 'POST' and (str(pk) not in request.COOKIES):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             new = Review(text=form.cleaned_data['text'], product=product)
#             new.save()
#             response = redirect('/')
#             response.set_cookie(str(pk), 'test')
#             return response
#
#     else:
#         form = ReviewForm
#     context = {
#         'form': form,
#         'product': product,
#         'reviews': reviews,
#     }
#
#     return render(request, template, context)

def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.all()
    if request.method == 'POST' and not request.session.get(pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            new = Review(text=form.cleaned_data['text'], product=product)
            new.save()
            return redirect('/')
    else:
        form = ReviewForm
    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
    }

    return render(request, template, context)
