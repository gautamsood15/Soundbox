from django.db import models

# Create your models here.

class Music(models.Model):
      title=models.CharField(max_length=500)
      artist=models.CharField(max_length=500)
      album=models.ForeignKey('Album', null=True, blank=True, on_delete=models.SET_NULL)
      time_length=models.DecimalField(blank=True, max_digits=20, decimal_places=2)
      audio_file=models.FileField(upload_to="musics")
      cover_image=models.ImageField(upload_to="music_image/")

      def save(self, *args, **kwargs):
        if not self.time_length:
            # logic for getting music length here
            pass
        return super().save(*args, **kwargs)


class Album(models.Model):
    name=models.CharField(max_length=500)