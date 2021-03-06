from django.conf.urls import url

from kodkollektivet import github
from kodkollektivet import views

urlpatterns = [
    url(r'^projects/$', views.ProjectsListView.as_view(), name='projectslistview'),
    url(r'^board/$', views.BoardTemplateView.as_view(), name='boardtemplateview'),
    url(r'^thanks/$', views.ThanksTemplateView.as_view(), name='thankstemplateview'),
    url(r'^project/(?P<slug>\S+)/$',
        views.ProjectsDetailView.as_view(), name="projectdetailview"),
    url(r'^events/$', views.EventsListView.as_view(), name="eventslistview"),
    url(r'^event/(?P<slug>\S+)/$',
        views.EventsDetailView.as_view(), name="eventdetailview"),
    url(r'^contributor/(?P<slug>\S+)/$',
        views.ContributorDetailView.as_view(), name="contributordetailview"),
    url(r'^github/webhook$', github.GithubHook.as_view(), name='githubwebhook'),
]
