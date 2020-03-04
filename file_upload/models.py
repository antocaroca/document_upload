from django.db import models

class Document(models.Model):
    title = models.CharField("Título", max_length=100)
    date = models.DateField("Fecha")
    pdf = models.FileField(upload_to='docs/pdfs')
    cover = models.ImageField("Foto", upload_to='docs/covers', null='True', blank='True')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
