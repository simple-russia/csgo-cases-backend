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
        return self.name


# CSGO weapon
class Weapon (models.Model):
    id = models.AutoField(primary_key=True)
    style = models.CharField(max_length=45, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.CharField(max_length=150, null=False, blank=False)
    # foreign keys
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)


    statrak = models.BooleanField(blank=False, null=False)


    class Meta:
        db_table = "weapon"

    def __str__(self):
        return  f"{self.type_id} {self.style}"





# CSGO description
class Description (models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    weapon_id = models.ForeignKey(Weapon, on_delete=models.CASCADE)

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
        return  f"{self.language} - {self.weapon_id}"


# CSGO case
class Case (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=45, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.CharField(max_length=150, null=False, blank=False)

    is_special = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        db_table = "case"
    
    def __str__(self):
        return self.name

# case has weapon
class Case_has_weapon (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    weapon_id = models.ForeignKey(Weapon, on_delete=models.CASCADE)

    class Meta:
        db_table = "case_has_weapon"
        unique_together = (("case_id", "weapon_id"),)
    
    def __str__(self):
        return  f"{self.case_id} -> {self.weapon_id}"



