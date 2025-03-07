from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Curriculum
from ..forms import CurriculumForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CurriculumListView(ListView):
    model = Curriculum
    template_name = "experiences/curriculum_list.html"
    paginate_by = 20
    context_object_name = "curriculum_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CurriculumListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CurriculumListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CurriculumListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CurriculumListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CurriculumListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CurriculumListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CurriculumListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CurriculumListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CurriculumListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CurriculumListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CurriculumListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CurriculumListView, self).get_template_names()


class CurriculumDetailView(DetailView):
    model = Curriculum
    template_name = "experiences/curriculum_detail.html"
    context_object_name = "curriculum"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CurriculumDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CurriculumDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CurriculumDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CurriculumDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CurriculumDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CurriculumDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CurriculumDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CurriculumDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CurriculumDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CurriculumDetailView, self).get_template_names()


class CurriculumCreateView(CreateView):
    model = Curriculum
    form_class = CurriculumForm
    # fields = ['title', 'description', 'is_active']
    template_name = "experiences/curriculum_create.html"
    success_url = reverse_lazy("curriculum_list")

    def __init__(self, **kwargs):
        return super(CurriculumCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CurriculumCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CurriculumCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CurriculumCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CurriculumCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CurriculumCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CurriculumCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CurriculumCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CurriculumCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CurriculumCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CurriculumCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CurriculumCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CurriculumCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("experiences:curriculum_detail", args=(self.object.pk,))


class CurriculumUpdateView(UpdateView):
    model = Curriculum
    form_class = CurriculumForm
    # fields = ['title', 'description', 'is_active']
    template_name = "experiences/curriculum_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "curriculum"

    def __init__(self, **kwargs):
        return super(CurriculumUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CurriculumUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CurriculumUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CurriculumUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CurriculumUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CurriculumUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CurriculumUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CurriculumUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CurriculumUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CurriculumUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CurriculumUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CurriculumUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CurriculumUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CurriculumUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CurriculumUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CurriculumUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CurriculumUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("experiences:curriculum_detail", args=(self.object.pk,))


class CurriculumDeleteView(DeleteView):
    model = Curriculum
    template_name = "experiences/curriculum_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "curriculum"

    def __init__(self, **kwargs):
        return super(CurriculumDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CurriculumDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CurriculumDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CurriculumDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CurriculumDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CurriculumDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CurriculumDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CurriculumDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CurriculumDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CurriculumDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CurriculumDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("experiences:curriculum_list")
