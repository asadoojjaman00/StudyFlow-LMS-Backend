from django.db import models
from .category import Category
from users.models.User_model import User
from django.utils.text import slugify

class Course(models.Model):
    class TypeChoices(models.TextChoices):
        FREE = 'free', 'Free'
        PAID = 'paid', 'Paid'
        TRIAL = 'trial', 'Trial'
        DEMO = 'demo', 'Demo'

    title          = models.CharField(max_length=250)
    slug           = models.SlugField(max_length=280, unique=True, blank=True)
    description    = models.TextField()
    thumbnail      = models.ImageField(upload_to='course/thumbnail/', blank=True, null=True)
    is_published   = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    total_enrolled = models.PositiveIntegerField(default=0)
    price          = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    type           = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.TRIAL
    )
    category       = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    instructors    = models.ManyToManyField(
        User,
        related_name='courses_as_instructor',
        limit_choices_to= {'role':'instructor'},
        blank=True
    )
    created_by     = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_courses',
        limit_choices_to={'role':'instructor'}
    )
    

    class Meta:
        verbose_name_plural = 'Courses'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title