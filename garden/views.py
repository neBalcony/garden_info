from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card

@login_required
def tags_list(request):
    cards = Card.objects.all()
    return render(request, 'tags_list.html', {'cards': cards})


@login_required
def card_detail(request, id):
    card = get_object_or_404(Card, id=id)

    if request.method == 'POST':
        content = request.POST.get('card_content')
        card.content = content
        card.save()

    return render(request, 'card_detail.html', {'card': card})
