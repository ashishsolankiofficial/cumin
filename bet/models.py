from django.db import models
from utils.model_utils import get_ext_id

from players.models import BusinessUnit, User
from playable.models import MultiChoice, Choice


class MultiChoiceBetResolver(models.Model):
    resolved = models.BooleanField(default=False)
    playable = models.ForeignKey(MultiChoice, related_name='resolver', on_delete=models.CASCADE)
    business_unit = models.ForeignKey(BusinessUnit, related_name='resolver', on_delete=models.CASCADE)


# Create your models here.
class MultiChoiceBet(models.Model):
    ext_id = models.CharField(max_length=10)
    choice = models.ForeignKey(Choice, related_name='bets', on_delete=models.CASCADE)
    resolver = models.ForeignKey(MultiChoiceBetResolver, related_name='bets', on_delete=models.CASCADE)
    player = models.ForeignKey(User, related_name='bets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)