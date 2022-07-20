from django.shortcuts import render, HttpResponse 
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import TopicForm , EntryForm
from .models import Topic, Entry

# Create your views here.

def index(request):
	"""主页"""
	return render(request, 'learning_logs/index.html')

@login_required #user's topics
def topics(request):                                                         
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required #user's topics
def topic(request, topic_id):
    """show single topic and self.entrise"""
    topic = Topic.objects.get(id=topic_id)
        
    #check
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required #user's topics
def new_topic(request):
    """add new topic"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
           new_topic = form.save(commit=False)
           new_topic.owner = request.user
           new_topic.save()
           return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required #user's topics
def new_entry(request, topic_id):
    """add new entry in select_topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """create a  empty tablelist"""
        form = EntryForm()
    else:
        # process to post put data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required #user's topics
def edit_entry(request, entry_id):
    """edit there entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    #check
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # first request , use there entry full the post
        form = EntryForm(instance=entry)
    else:
        #POST offer date , process to data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
