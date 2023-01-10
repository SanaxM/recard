from django.urls import path
from . import views

urlpatterns = [
    #landing page = all the cue cards displayed
    path(
        "",
        views.CueCardListView.as_view(),
        name="cuecard-list"
    ),
    path(
        "new", 
        views.CueCardCreateView.as_view(), 
        name="cuecard-create"),
    #primary key (pk) to distinguish which database entry we want to modify. automatically assigned. CueCardUpdateView will return info pertaining to pk
    path(
        "edit/<int:pk>", 
        views.CueCardUpdateView.as_view(), 
        name="cuecard-update"),
    #int:box_num: django gives the box num to the view
    path(
        "box/<int:box_num>", 
        views.BoxView.as_view(), 
        name="box"
        ),
]
