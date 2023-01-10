from django import template
from recards.models import BOXES, CueCard

#obj of library to register tag
register = template.Library()

#use the decorator of .inclusion_tag to make boxes_as_links an inclusion tag
@register.inclusion_tag("recards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        #tracks cards per box
        card_count = CueCard.objects.filter(box=box_num).count()
        #add to the boxes list a dict (kv pair) of the box num and card count
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    #return the boxes list casted as dictionary
    return {"boxes": boxes}