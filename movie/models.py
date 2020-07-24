from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    released = models.DateField(blank=True, null=True, default=None)
    is_released = models.BooleanField(default=False)
    cover = models.FileField(upload_to='covers/', null=True, blank=True)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.star
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    star = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
