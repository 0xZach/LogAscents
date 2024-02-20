from django.db import models    
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Grade(models.Model):
    
    # Attributs
    
    name = models.CharField(max_length=3)
    value = models.IntegerField(default=0)


    # Methods

    
    def __str__(self):
        return self.name





# ---------------------------------------- #





class Ascent(models.Model):
    
    # Attributs
    
    name = models.CharField(max_length=100, default= "")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    video = models.FileField(
            upload_to='videos/', # determines which subfolder of MEDIA_ROOT will recieve the uploaded file
            null=True,
            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
            )
    date_uploaded = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=100, default="")


    # Methods

    # edit of the pre-existing "save" function to allow auto-replacing the name if nothing was given originally
    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.grade.name + ' (' + self.date_uploaded.date().__str__() + ')'
        super(Ascent, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name

# ascent test object: 
# Ascent(grade = Grade.Objects.get(name="7A"), video="/home/sylvain/Downloads/mmhmh.mp4", date_uploaded=timezone.now)