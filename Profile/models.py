from django.db import models
from django.contrib.auth.models import User
class ProfileModel(models.Model):
    user= models.ForeignKey(User, on_delete= models.SET(-1))
    address = models.CharField(max_length = 225, null= False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add= True)

    def _str_(self):
        return self.user

