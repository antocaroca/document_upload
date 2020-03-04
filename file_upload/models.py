from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    pdf = models.FileField(upload_to='docs/pdfs')
    cover = models.ImageField(upload_to='docs/covers', null='True', blank='True')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
