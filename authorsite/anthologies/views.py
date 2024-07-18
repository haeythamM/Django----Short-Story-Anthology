from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Collection, Cover, Story
from .forms import CollectionForm, CoverForm, StoryForm

class CollectionList(ListView):
    model = Collection
    template_name = 'collection-index.html.django'
    context_object_name = 'collections'

class CollectionDetail(DetailView):
    model = Collection
    template_name = 'collection-detail.html.django'
    context_object_name = 'collection'

class CollectionCreate(CreateView):
    model = Collection
    template_name = 'add-collection.html.django'
    fields = CollectionForm.Meta.fields
    success_url = reverse_lazy('collections-home')

class CollectionUpdate(UpdateView):
    model = Collection
    template_name = 'edit-collection.html.django'
    fields = CollectionForm.Meta.fields
    success_url = reverse_lazy('collections-home')

class CollectionDelete(DeleteView):
    model = Collection
    template_name = 'delete-collection.html.django'
    success_url = reverse_lazy('collections-home')

class CoverCreate(CreateView):
    model = Cover
    template_name = 'add-cover.html.django'
    fields = CoverForm.Meta.fields
    success_url = reverse_lazy('collections-home')
    def form_valid(self, form):
        form.instance.collection_id = self.kwargs.get('pk')
        return super(CoverCreate, self).form_valid(form)

class StoryCreate(CreateView):
    model = Story
    template_name = 'add-story.html.django'
    fields = StoryForm.Meta.fields
    success_url = reverse_lazy('collections-home')

    def form_valid(self, form):
        form.instance.collection_id = self.kwargs.get('pk')
        return super(StoryCreate, self).form_valid(form)
