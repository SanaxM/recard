from django.db import models

#creating constant vars for the number of boxes
NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

#each card will be stored in the database with 4 attributes: concept, answer, box (where its located), date created
class CueCard(models.Model):
    #initialize the two char fields of the cue cards to a certain length
    concept = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    #initalize int fields: which box number we can select (1-5) and the default box # (first box)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES), 
        default=BOXES[0],
        )
    
    #date of the card created is also stored
    date_created = models.DateTimeField(auto_now_add=True)
    
    #change the string representation of this class to just be the concept (like a normal cue card)
    def __str__(self):
        return self.concept
    
    #moves the card either up a box or to box 1 depending on if user knows the answer to the cue card
    def move(self, solved):
        #if solved = true, then the box number is increased, else it is set to box 1
        new_box = self.box + 1 if solved else BOXES[0]
        
        if new_box in BOXES:
            self.box = new_box
            self.save()
            
        return self