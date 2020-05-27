from django.db import models

class Movie (models.Model):
	title = models.CharField(max_length=80, blank=False, unique=True)
	year = models.PositiveSmallIntegerField(default=2000)
	descript = models.TextField(default="")
	premiere = models.DateField(null=True, blank=True)
	imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	poster = models.ImageField(upload_to="poster", null=True, blank=True)

	def __str__(self):
		return self.title_with_year()

	def title_with_year(self):
		return "{} ({})".format(self.title, self.year)


