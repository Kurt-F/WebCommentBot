from django.db import models


# A website registered with the bot
class UserSite(models.Model):
    url = models.CharField(max_length=2000)


# A telegram user registered with a website
class TelegramUser(models.Model):
    telegram_name = models.CharField(max_length=32)
    # This forces a 1-1 relationship between topics and users
    # If "NULL" then all unmatched topics are sent to this user
    topic = models.CharField(max_length=256)
    # The site associated with the user
    site = models.ForeignKey(UserSite, on_delete=models.CASCADE, default=None)
