from django.db import models

from accounts.models import Account


class Gender(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Perfume(models.Model):
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=255, blank=True, null=True)
    first_note = models.CharField(max_length=255, blank=True, null=True)
    heart_note = models.CharField(max_length=255, blank=True, null=True)
    last_note = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='perfume_images/', blank=True, null=True,
                              default='/perfume_images/perfume_default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class ReviewReply(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user} on {self.review}"


class Offer(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to='offer_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='offer_images/', blank=True, null=True)

    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price_per_ml = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.perfume.name} - {self.seller.full_name()}"
