from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BlogPost, BlogCategory
from .forms import BlogPostForm


@login_required
def create_blog(request):
    """Doctor can create a new blog post"""
    # Check if user is a doctor
    if request.user.profile.role != 'Doctor':
        return HttpResponseForbidden("Only doctors can create blog posts")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('doctor_blogs')
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def doctor_blogs(request):
    """Doctor can see their own blog posts (both draft and published)"""
    if request.user.profile.role != 'Doctor':
        return HttpResponseForbidden("Only doctors can access this page")

    blogs = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/doctor_blogs.html', {'blogs': blogs})


@login_required
def edit_blog(request, blog_id):
    """Doctor can edit their own blog post"""
    blog = get_object_or_404(BlogPost, id=blog_id)

    if blog.author != request.user:
        return HttpResponseForbidden("You can only edit your own blogs")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('doctor_blogs')
    else:
        form = BlogPostForm(instance=blog)

    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request, blog_id):
    """Doctor can delete their own blog post"""
    blog = get_object_or_404(BlogPost, id=blog_id)

    if blog.author != request.user:
        return HttpResponseForbidden("You can only delete your own blogs")

    if request.method == 'POST':
        blog.delete()
        return redirect('doctor_blogs')

    return render(request, 'blog/delete_blog.html', {'blog': blog})


@login_required
def patient_blogs(request):
    """Patient can see all published blog posts by category"""
    if request.user.profile.role != 'Patient':
        return HttpResponseForbidden("Only patients can access this page")

    categories = BlogCategory.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        blogs = BlogPost.objects.filter(
            category_id=selected_category,
            is_draft=False
        ).order_by('-created_at')
        selected_cat_obj = get_object_or_404(BlogCategory, id=selected_category)
    else:
        blogs = BlogPost.objects.filter(is_draft=False).order_by('-created_at')
        selected_cat_obj = None

    return render(request, 'blog/patient_blogs.html', {
        'blogs': blogs,
        'categories': categories,
        'selected_category': selected_category,
        'selected_cat_obj': selected_cat_obj,
    })


def blog_detail(request, blog_id):
    """View blog post detail"""
    blog = get_object_or_404(BlogPost, id=blog_id)

    # If blog is draft, only author can view it
    if blog.is_draft:
        if not request.user.is_authenticated or blog.author != request.user:
            return HttpResponseForbidden("This blog post is not available")

    return render(request, 'blog/blog_detail.html', {'blog': blog})
