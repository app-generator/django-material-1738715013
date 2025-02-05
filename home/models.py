# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Document(models.Model):

    #__Document_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    file_doc = models.CharField(max_length=255, null=True, blank=True)

    #__Document_FIELDS__END

    class Meta:
        verbose_name        = _("Document")
        verbose_name_plural = _("Document")


class Jogo(models.Model):

    #__Jogo_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField()

    #__Jogo_FIELDS__END

    class Meta:
        verbose_name        = _("Jogo")
        verbose_name_plural = _("Jogo")



#__MODELS__END
