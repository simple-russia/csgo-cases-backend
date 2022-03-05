from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# CSGO collection
class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = "collection"
    
    def __str__(self):
        return self.name

# CSGO type
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False, blank=False)

    class Meta:
        db_table = "type"

    def __str__(self):
        return self.name


# CSGO color
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    hex = models.CharField(max_length=6, null=False, blank=False)

    class Meta:
        db_table = "color"
    
    def __str__(self):
        return f"{self.name} {self.hex}"


# CSGO weapon
class Weapon (models.Model):
    id = models.AutoField(primary_key=True)
    style = models.CharField(max_length=45, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.CharField(max_length=150, null=False, blank=False)
    statrak = models.BooleanField(blank=False, null=False)
    # foreign keys
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)




    class Meta:
        db_table = "weapon"

    def __str__(self):
        return  f"{self.type} {self.style}"





# CSGO description
class Description (models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)

    RUSSIAN = 'ru'
    ENGLISH = 'en'
    SPANISH = 'es'
    PORTUGUESE = 'pt'
    GERMAN = 'de'

    LANGUAGE_CHOICES = [
        (RUSSIAN, 'Russian'),
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
        (PORTUGUESE, 'Portuguese'),
        (GERMAN, 'German'),
    ]
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, null=False, blank=False)

    class Meta:
        db_table = "description"
    
    def __str__(self):
        return  f"{self.language} - {self.weapon}"


# CSGO case
class Case (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=45, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.CharField(max_length=150, null=False, blank=False)
    is_available = models.BooleanField(default=True)
    link_name = models.CharField(max_length=45, blank=False, null=False)

    is_special = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        db_table = "case"
    
    def __str__(self):
        return self.name

# case has weapon
class Case_has_weapon (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    rarity = models.IntegerField(blank=False, null=False)
    index = models.IntegerField()

    class Meta:
        db_table = "case_has_weapon"
        unique_together = (("case", "weapon"),)
    
    def __str__(self):
        return  f"{self.case} -> {self.weapon}"

class Action_type (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        db_table = "action_type"
    
    def __str__(self):
        return  f"{self.name}"

class Action (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    time = models.BigIntegerField() # unix time
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Action_type, on_delete=models.CASCADE)
    object_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = "action"
    
    def __str__(self):
        return  f"{self.user} {self.type}"


