from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Card, NFCTag
from .forms import CardForm, NFCTagForm

# доступ к карточке — только авторизованные пользователи
@login_required
def card_detail(request, slug):
    card = get_object_or_404(Card, slug=slug)

    # если пришёл POST — сохраняем изменения (редактирование)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_detail', slug=card.slug)
    else:
        form = CardForm(instance=card)

    return render(request, 'card_detail.html', {'card': card, 'form': form})

# проверка на администратора (staff)
def is_staff(user):
    return user.is_active and user.is_staff

@user_passes_test(is_staff)
def tags_list(request):
    tags = NFCTag.objects.select_related('card').all()
    return render(request, 'tags_list.html', {'tags': tags})

@user_passes_test(is_staff)
def tag_create(request):
    if request.method == 'POST':
        form = NFCTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags_list')
    else:
        form = NFCTagForm()
    return render(request, 'tag_create.html', {'form': form})

@user_passes_test(is_staff)
def card_create(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            return redirect('tags_list')
    else:
        form = CardForm()
    return render(request, 'card_create.html', {'form': form})

@login_required
def card_detail(request, id):
    card = get_object_or_404(Card, id=id)
    tag = card.nfc_tags.first() 
    # если пришёл POST — сохраняем изменения (редактирование)
    if request.method == 'POST':
        content = request.POST.get('card_content')
        card.content = content
        card.save()
    else:
        form = CardForm(instance=card)

    return render(request, 'card_detail.html', {'card': card, 'tag': tag})
