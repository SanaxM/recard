from django import forms

#form to check if a cue card has been solved
class CueCardCheckForm(forms.Form):
    #primary key of the cue card (identifier)
    card_id = forms.IntegerField(required=True)
    #whether it has been solved or not, initially set to false as not sure if it was solved yet
    solved = forms.BooleanField(required=False)