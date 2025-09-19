from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Card, NFCTag
from .forms import CardForm, NFCTagForm

@login_required
def tags_list(request):
    tags = NFCTag.objects.select_related('card').all()
    return render(request, 'tags_list.html', {'tags': tags})


@login_required
def card_detail(request, id):
    card = get_object_or_404(Card, id=id)
    tag = card.nfc_tags.first() 

    if request.method == 'POST':
        content = request.POST.get('card_content')
        card.content = content
        card.save()
    else:
        form = CardForm(instance=card)

    return render(request, 'card_detail.html', {'card': card, 'tag': tag})
