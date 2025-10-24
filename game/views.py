from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import TruthPrompt, DarePrompt
import random


def get_random_truth():
    """Get a random active truth prompt"""
    truths = TruthPrompt.objects.filter(is_active=True)
    if truths:
        return random.choice(truths)
    return None


def get_random_dare():
    """Get a random active dare prompt"""
    dares = DarePrompt.objects.filter(is_active=True)
    if dares:
        return random.choice(dares)
    return None


class GameView(View):
    def get(self, request):
        """Display the main game interface"""
        context = {
            'current_prompt': None,
            'prompt_type': None,
        }
        return render(request, 'game/index.html', context)

    def post(self, request):
        """Handle truth or dare selection"""
        action = request.POST.get('action')
        current_prompt = None
        prompt_type = None

        if action == 'truth':
            current_prompt = get_random_truth()
            prompt_type = 'truth'
        elif action == 'dare':
            current_prompt = get_random_dare()
            prompt_type = 'dare'

        context = {
            'current_prompt': current_prompt,
            'prompt_type': prompt_type,
        }
        return render(request, 'game/index.html', context)
