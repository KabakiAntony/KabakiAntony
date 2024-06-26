from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    thumb = models.ImageField(blank=True)
    url = models.URLField(max_length=400, unique=True)

    class Meta:
        abstract = True


class Me(BaseModel):
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Me"
    

class Projects(BaseModel):
    github_url = models.URLField(max_length=400, unique=True, null=True)

    def snippet(self):
        return self.description[:200] + " ..."

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Projects"
    

class Blogs(BaseModel):
    def snippet(self):
        return self.description[:150] + " ..."

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Articles"
