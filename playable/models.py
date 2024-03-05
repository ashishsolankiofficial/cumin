from django.db import models
from utils.model_utils import get_ext_id

class PlayableCategories(models.Model):
    name = models.CharField(max_length=100)

class PlayableGroup(models.Model):

    ext_id = models.CharField(max_length=10)
    category = models.ForeignKey(PlayableCategories, related_name='playable_groups', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)

class Playable(models.Model):
    ext_id = models.CharField(max_length=10)
    group = models.ForeignKey(PlayableGroup, related_name='playables', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    disable_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)


class MultiChoice(Playable):
    description = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(MultiChoice, related_name='choices', on_delete=models.CASCADE, null=True)
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
