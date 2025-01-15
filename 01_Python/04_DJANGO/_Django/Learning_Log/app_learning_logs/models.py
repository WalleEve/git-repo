from django.db import models

# Create your models here.

class Topic(models.Model):
	""" A Topic user is learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		""" Return a string representation of the model. """
		return self.text 


class Entry(models.Model):
	""" Something specific learned about a topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	"""
	# Option: Cascade deletes
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

	# Option: Set foreign key to NULL
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

	# Option: Prevent deletion of the topic if it is referenced
	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	"""
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text[:50] + "..."