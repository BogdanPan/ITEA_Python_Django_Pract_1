from django.db import models
from autoslug import AutoSlugField


class Post(models.Model):
	title = models.TextField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to='Post_images', blank=True, null=True)
	slug = AutoSlugField(populate_from='title', null=True, unique=True, allow_unicode=True)

	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	@classmethod
	def find_by_slug(cls, slug):
		return cls.objects.filter(slug=slug).first()

	@classmethod
	def get_all_url_names(cls):
		name_list = []
		for obj in cls.objects.all():
			name_list.append(obj.name)
		return name_list

	def get_number_of_posts(self):
		return len(Comment.find_by_art(self))

	def __str__(self):
		return f"{self.title}, {self.title}"

	def save(self, *args, **kwargs):
		self.slug = None
		super().save(*args, **kwargs)


class Comment(models.Model):
	post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
	username = models.CharField(max_length=255)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	@classmethod
	def find_by_art(cls, post):
		return cls.objects.filter(post=post)
