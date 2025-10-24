from django.test import TestCase, Client
from django.urls import reverse
from .models import TruthPrompt, DarePrompt
from .views import GameView


class TruthPromptModelTest(TestCase):
    def test_truth_prompt_creation(self):
        truth = TruthPrompt.objects.create(text="What's your biggest fear?")
        self.assertEqual(truth.text, "What's your biggest fear?")
        self.assertTrue(truth.is_active)

    def test_truth_prompt_string_representation(self):
        truth = TruthPrompt.objects.create(text="Test truth question")
        self.assertEqual(str(truth), "Test truth question")


class DarePromptModelTest(TestCase):
    def test_dare_prompt_creation(self):
        dare = DarePrompt.objects.create(text="Do 10 jumping jacks")
        self.assertEqual(dare.text, "Do 10 jumping jacks")
        self.assertTrue(dare.is_active)

    def test_dare_prompt_string_representation(self):
        dare = DarePrompt.objects.create(text="Test dare challenge")
        self.assertEqual(str(dare), "Test dare challenge")


class GameViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test data
        TruthPrompt.objects.create(text="Test truth 1")
        TruthPrompt.objects.create(text="Test truth 2")
        DarePrompt.objects.create(text="Test dare 1")
        DarePrompt.objects.create(text="Test dare 2")

    def test_game_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Truth")
        self.assertContains(response, "Dare")

    def test_get_truth_returns_random_truth(self):
        response = self.client.post('/', {'action': 'truth'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "Test truth 1" in response.content.decode() or
            "Test truth 2" in response.content.decode()
        )

    def test_get_dare_returns_random_dare(self):
        response = self.client.post('/', {'action': 'dare'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "Test dare 1" in response.content.decode() or
            "Test dare 2" in response.content.decode()
        )


class GameLogicTest(TestCase):
    def setUp(self):
        # Create test prompts
        self.truth1 = TruthPrompt.objects.create(text="Truth 1")
        self.truth2 = TruthPrompt.objects.create(text="Truth 2")
        self.dare1 = DarePrompt.objects.create(text="Dare 1")
        self.dare2 = DarePrompt.objects.create(text="Dare 2")

    def test_random_truth_selection(self):
        from .views import get_random_truth
        truth = get_random_truth()
        self.assertIn(truth.text, ["Truth 1", "Truth 2"])

    def test_random_dare_selection(self):
        from .views import get_random_dare
        dare = get_random_dare()
        self.assertIn(dare.text, ["Dare 1", "Dare 2"])
