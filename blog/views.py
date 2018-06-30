from django.shortcuts import render

#view
def post_list(request):
    return render(request, 'blog/post_list.html', {})
