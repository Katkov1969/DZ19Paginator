from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    """Отображает список постов с пагинацией."""
    post_list = Post.objects.all().order_by('-pub_date')

    # Получаем количество постов на странице из GET-параметра, по умолчанию 5
    per_page = request.GET.get('per_page', 5)

    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'posts': posts, 'per_page': per_page})



