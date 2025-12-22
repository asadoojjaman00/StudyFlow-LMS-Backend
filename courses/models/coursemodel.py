from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from users.models.User_model import User
from .category import Category
import uuid

class Course(models.Model):

    class TypeChoices(models.TextChoices):
        FREE = 'free', 'Free'
        PAID = 'paid', 'Paid'

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='course/thumbnail/', blank=True, null=True)

    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.FREE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_courses"
    )

    instructors = models.ManyToManyField(
        User,
        related_name="teaching_courses",
        blank=True
    )

    description = models.TextField()
    batch = models.CharField(max_length=30)

    demo_class_video = models.URLField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )
    discount_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    enrollment_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.type == self.TypeChoices.PAID and self.price is None:
            raise ValidationError({"price": "Paid course must have a price."})

        if self.price and self.discount_price:
            if self.discount_price >= self.price:
                raise ValidationError({
                    "discount_price": "Discount must be less than price."
                })

    def __str__(self):
        return self.title