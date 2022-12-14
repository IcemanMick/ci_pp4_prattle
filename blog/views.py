# Code Credit structure to ITTIB by CI, mix of ITTIB and custom
# values for lines 5 to 30


from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Topic


class TopicList(generic.ListView):
    model = Topic
    queryset = Topic.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class ThreadList(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Topic.objects.filter(status=1)
        topic = get_object_or_404(queryset, slug=slug)
        threads = topic.threads.filter(approved=True).order_by('-created_on')

        return render(
            request, "thread_list.html", {
                "post": topic,
                "threads": threads,
                },
        )
