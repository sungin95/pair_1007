from django.shortcuts import render, redirect


from post.forms import PostForm
from post.models import Post
from .forms import ReviewForm
from . models import Review



# Create your views here.
def main(request):
    review = Post.objects.order_by('-pk')
    context ={
        'post' : review,
    }
    return render(request, "reviews/main.html", context)

def index(request):
    review = Review.objects.order_by('-pk')
    context ={
        'reviews' : review
    }
    
    return render(request, "reviews/index.html", context)

def new(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("review:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/new.html", context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review' : review
    }

    return render(request,'reviews/detail.html',context)

def update(request,pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("review:index")

    review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request,'reviews/update.html',context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("review:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/new.html", context)

def admin(request):
    review = Post.objects.order_by('-pk')
    context ={
        'post' : review,
    }
    return render(request,'reviews/aadmin.html', context)

def admin_create(request):
    if request.method == "POST":
        review_form = PostForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("review:aadmin")
    else:
        review_form = PostForm()
    context = {
        "Post_Form": review_form,
    }
    return render(request, "reviews/admin_create.html", context)