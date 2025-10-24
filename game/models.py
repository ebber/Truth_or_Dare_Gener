from django.db import models


class TruthPrompt(models.Model):
    text = models.TextField(help_text="The truth question to ask")
    is_active = models.BooleanField(default=True, help_text="Whether this prompt is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']
        verbose_name = "Truth Prompt"
        verbose_name_plural = "Truth Prompts"


class DarePrompt(models.Model):
    text = models.TextField(help_text="The dare challenge to perform")
    is_active = models.BooleanField(default=True, help_text="Whether this prompt is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']
        verbose_name = "Dare Prompt"
        verbose_name_plural = "Dare Prompts"
