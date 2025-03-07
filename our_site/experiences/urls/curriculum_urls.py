from django.urls import re_path  
from ..views import (CurriculumListView, CurriculumCreateView, CurriculumDetailView,
                     CurriculumUpdateView, CurriculumDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/$',  # NOQA
        login_required(CurriculumCreateView.as_view()),
        name="curriculum_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(CurriculumUpdateView.as_view()),
        name="curriculum_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(CurriculumDeleteView.as_view()),
        name="curriculum_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        CurriculumDetailView.as_view(),
        name="curriculum_detail"),

    re_path(r'^$',
        CurriculumListView.as_view(),
        name="curriculum_list"),
]
