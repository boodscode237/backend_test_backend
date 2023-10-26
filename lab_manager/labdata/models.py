from django.db import models


class Material(models.Model):
    mat_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    synonyms = models.TextField(max_length=255)
    chem_form = models.TextField(max_length=255)
    cas_num = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    art_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)

    def __str__(self):
        return self.email


class Nanoparticle(models.Model):
    id = models.AutoField(primary_key=True)
    np_str = models.TextField(max_length=255)
    size = models.FloatField()
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    mat = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.np_str


class Synthesis(models.Model):
    id = models.AutoField(primary_key=True)
    np = models.ForeignKey(Nanoparticle, on_delete=models.CASCADE)
    method = models.TextField(max_length=255)
    article_id = models.IntegerField()

    def __str__(self):
        return f"Synthesis for {self.np.np_str}"


class Nova(models.Model):
    id = models.AutoField(primary_key=True)
    np = models.ForeignKey(Nanoparticle, on_delete=models.CASCADE)
    method = models.TextField(max_length=255)
    absorbat = models.TextField(max_length=255)
    pore_size = models.FloatField()
    density = models.FloatField()
    ads_desorb_curve = models.FileField()
    pore_distr_curve = models.FileField()

    def __str__(self):
        return f"NOVA for {self.np.np_str}"
