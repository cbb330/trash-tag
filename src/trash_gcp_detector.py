import io
import os
import enum

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Create the enum class
class Trash(enum.Enum):
	CAN = 1
	BOTTLE = 2
	OTHER = 3

def get_labels(file_path):
	'''
		This function receives the path to the image file. 
		Returns the list of labels associated to the image using GCP label detector. 
	'''

	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    file_path)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Removes the image file from memory to receive next one
	# os.remove('../assets/trash_image.jpg')

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	return labels


def get_type(labels, Trash=Trash):
	'''
		This function receives a list of labels associated to image processed.
		Returns the type either 'can' or a 'bottle'. 
	'''

	n_can_labels = 0
	n_bottle_labels = 0
	n_other_labels = 0

	for label in labels:
		label = str(label)
		if ('can' in label.lower()):
			n_can_labels += 1
		elif ('bottle' in label.lower()):
			n_bottle_labels += 1
		else:
			n_other_labels += 1

	if (n_can_labels + n_bottle_labels == 0):
		trash_type = Trash.OTHER
	elif (n_can_labels > n_bottle_labels):
		trash_type = Trash.CAN
	elif (n_can_labels <= n_bottle_labels):
		trash_type = Trash.BOTTLE
	
	return (trash_type.name)

def init(file_path):
	'''
	    This function receives trash image object and Returns trash type
	'''

	trash_labels = get_labels(file_path)
	trash_type = get_type(trash_labels)

	return str(trash_type.lower())


    
