from django.db import connection
from django.shortcuts import render_to_response
import simplejson as json

def upload_table(request):
	"""
	Renders csv upload form and creates document table in db
	"""


def update_fields(request):
	"""
	Updates uploaded table fields in TableField class
	"""


def edit_table(request):
	"""
	Enables editing of document properties
	"""


def edit_fields(request):
	"""
	Enables editing of document field properties
	"""


def visualise_table(request):
	"""
	Enables visualization of document as grid
	"""


def chart_table(request):
	"""
	Enables visualization of document as chart
	"""


def download_table(request):
	"""
	Enables download of document as csv
	"""


def map_table(request):
	"""
	Joins document to spatial layer and publishes new table to geoserver
	"""
