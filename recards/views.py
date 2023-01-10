import random

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)
from .models import CueCard
from .forms import CueCardCheckForm

#create a class that displays (renders) the cue card onto the screen. inherit ListView properties
class CueCardListView(ListView):
    #set the model that we are referring to (our cue cards)
    model = CueCard
    #set the list of cuecards we want to iterate over, iterating in order of oldest card in ascending box order
    queryset = CueCard.objects.all().order_by("box", "-date_created")
    
class CueCardCreateView(CreateView):
    model = CueCard
    #the fields that need to inputted to create a new card
    fields = ["concept", "answer", "box"]
    #once the cue card is made, return back to the previous page to prevent changing pages
    success_url = reverse_lazy("cuecard-create")
    
class CueCardUpdateView(CueCardCreateView, UpdateView):
    success_url = reverse_lazy("cuecard-list")
    
class BoxView(CueCardListView):
    #overwriting the inherited template from CueCardListView
    template_name = "recards/box.html"
    #connect the checkForm with form_class
    form_class = CueCardCheckForm
    
    def get_queryset(self):
        #only return the cards in the box num selected (kwargs = keyword args, val is passed in)
        return CueCard.objects.filter(box=self.kwargs["box_num"])
    
    #get the box num as a parameter
    def get_context_data(self, **kwargs):
        #use the parent class' get_context_data method
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        #keep selecting random cards until there are no cards to review
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args , **kwargs):
        form = self.form_class(request.POST)
        #check if all the form info is valid or not
        if form.is_valid():
            #either get a cue card from the db or return an error that there is no more cards
            cuecard = get_object_or_404(CueCard, id=form.cleaned_data["cuecard_id"])
            #moves the card to the appropriate box dependent upon the button pressed
            cuecard.move(form.cleaned_data["solved"])
            
        return redirect(request.META.get("HTTP_REFERER"))