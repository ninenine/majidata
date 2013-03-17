from django.db import models

class Document(models.Model):
	"""
	A document is a MajiData csv made of column and rows
	"""
	doc_name = models.CharField(max_length=100, blank=True, null=True)
	doc_title = models.CharField(max_length=100, blank=True, null=True)
	abstract = models.TextField(_('abstract'), blank=True, null=True)
	published = models.BooleanField(default=True)
	doc_fields = models.ManyToManyField(TableField, blank=True, null=True)
	doc_file = models_CharField(max_length=100, blank=True, null=True)
	spatial_layer = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return "%s"	% self.doc_name

class TableField(models.Model):
	"""
	A tablefield is a column in a Majidata csv
	"""
	field_name = models.CharField(max_length=100, blank=True, null=True)
	field_label = models.CharField(max_length=100, blank=True, null=True)
	field_type = models.CharField(max_length=100, blank=True, null=True)
	visible = models.BooleanField(default=True)

	def __str__(self):
		return "%s" % self.field_name
