from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Topic


class TopicList(generic.ListView):
    model = Topic
    queryset = Topic.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class ThreadDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Topic.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if thread.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, 'thread.html', {
            "post": thread,
            "comments": comments,
            "liked": liked
        }
        )
