class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name
