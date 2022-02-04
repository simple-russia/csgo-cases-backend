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

    class Meta:
        db_table = "weapon"
    
    def __str__(self):
        return  f"{self.type_id} {self.style}"





# CSGO description


# CSGO case


# case has weapon




