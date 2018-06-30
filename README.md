## WebCommentBot

IMPORTANT: Unfinished.

This project is a django-powered telegram bot that makes it easy to
send comments from a website to the telegram account(s) of the site
administrator(s). Users register their site with the bot, set up message
forwarding, and write a simple HTML form that sends POST requests to the
bot url (host/sites/site_id) which are then parsed and routed to the
appropriate telegram accounts.


## Testing with existing bot
In telegram, message the @webutilbot and set up your website, following
the in-chat instructions. After your site is registered with the bot,
write your html form (with the correct fields, a sample form can be
found at templates/test_page.html) fill out a comment, submit it, and
it will be sent to your telegram account.

## Running with a unique bot
If desired, this repository can be cloned and used to run a bot with
identical function but on a different server. To do this, the bot
API key must be set either in an OS environment variable or in
key.txt in the botinterface folder, the database configured, and
otherwise set up to run as a django application.