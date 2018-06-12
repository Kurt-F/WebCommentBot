from django.db import models


# A website registered with the bot
class Site(models.Model):
    url = models.CharField(max_length=2000)


# A telegram user registered with a website
class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=32)
    # This forces a 1-1 relationship between topics and users
    topic = models.CharField(max_length=256)
    # The site associated with the user
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
