from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from twitter.forms import TweetCreationForm, MessageCreationForm
from twitter.models import Tweet


class IndexView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'base.html', {'tweets':tweets})


class AddTweetView(LoginRequiredMixin, View):

    def get(self, request):
        form = TweetCreationForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = TweetCreationForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.creator = request.user
            tweet.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})

class AddMessageView(LoginRequiredMixin, View):

    def get(self, request):
        form = MessageCreationForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MessageCreationForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = request.user
            message.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})


class UpdateTweetView(LoginRequiredMixin, UpdateView):
    model = Tweet
    fields = ['content']
    success_url = reverse_lazy('index')
    template_name = 'form.html'
