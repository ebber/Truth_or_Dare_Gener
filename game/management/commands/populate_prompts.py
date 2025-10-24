from django.core.management.base import BaseCommand
from game.models import TruthPrompt, DarePrompt


class Command(BaseCommand):
    help = 'Populate the database with initial Truth or Dare prompts'

    def handle(self, *args, **options):
        # Clear existing prompts
        TruthPrompt.objects.all().delete()
        DarePrompt.objects.all().delete()

        # Truth prompts
        truths = [
            "What's the most embarrassing thing that's ever happened to you?",
            "What's your biggest fear?",
            "What's the worst thing you've ever done?",
            "What's your most embarrassing childhood memory?",
            "What's the weirdest dream you've ever had?",
            "What's something you've never told anyone?",
            "What's your worst habit?",
            "What's the most trouble you've ever gotten into?",
            "What's your biggest regret?",
            "What's the strangest thing you've ever eaten?",
            "What's your most irrational fear?",
            "What's the worst grade you ever got?",
            "What's your most embarrassing moment in public?",
            "What's something you wish you could change about yourself?",
            "What's the weirdest thing you do when you're alone?",
            "What's your most embarrassing social media post?",
            "What's the worst lie you've ever told?",
            "What's your guilty pleasure?",
            "What's the most childish thing you still do?",
            "What's your biggest pet peeve?",
        ]

        # Dare prompts
        dares = [
            "Do 20 jumping jacks",
            "Sing your favorite song out loud",
            "Do your best impression of a famous person",
            "Dance with no music for 30 seconds",
            "Act like your favorite animal for 1 minute",
            "Do 10 push-ups",
            "Speak in an accent for the next 3 rounds",
            "Do a cartwheel or attempt one",
            "Recite the alphabet backwards",
            "Do your best stand-up comedy routine for 1 minute",
            "Pretend to be a news anchor and give a weather report",
            "Do the moonwalk across the room",
            "Sing 'Happy Birthday' in opera style",
            "Do your best robot dance",
            "Pretend to be a cat for 1 minute",
            "Do 15 sit-ups",
            "Speak like a pirate for the next 2 rounds",
            "Do your best runway model walk",
            "Pretend to be a superhero and describe your powers",
            "Do a magic trick (even if you don't know any)",
        ]

        # Create truth prompts
        for truth_text in truths:
            TruthPrompt.objects.create(text=truth_text)

        # Create dare prompts
        for dare_text in dares:
            DarePrompt.objects.create(text=dare_text)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(truths)} truth prompts and {len(dares)} dare prompts'
            )
        )