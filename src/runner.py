#!/usr/bin/env python3

from db import Database
from PIL import Image
import trash_gcp_detector as trash_detector
import face_comparer_aws as face_comparer
import face_detection as face_detector

trash_type = ""
person_uid = -1
db = Database()


def find_perfect_match(sources, n_targets, similarityThreshold=70.0):
	matched_sources = []
	targetFileDir = 'assets/target_images/target'

	if (len(sources) != 0):
		# Start comparing a source with all targets 
		for target_index in range(n_targets):

			# Extract the targetFile's binary object
			targetFilePath = targetFileDir + str(target_index) + '.jpg'
			targetFile = targetFilePath

			# Find all sources that have match_confidence levels above current threshold
			for source_index in range(len(sources)):
				sourceFile = sources[source_index][3] 

				match_confidence = face_comparer.get_face_comparison_confidence(sourceFile, targetFile, similarityThreshold)

				if (match_confidence >= similarityThreshold):
					matched_sources.append(sources[source_index])

			# Check if we have found the perfect_match, return it
			if (len(matched_sources) == 1):
				return matched_sources[0]
			# Otherwise repeat for all the matched sources
			else:
				find_perfect_match(matched_sources, n_targets, similarityThreshold+5)


def initiate_trash_type_detection():
	global trash_type

	##### TODO: Call opencv function to store trashimage
	trashFilePath = '../assets/trash_image/trash_image.jpg'
	trash_type = trash_detector.init(trashFilePath)


def get_sources():
	source_objects = list(db.getPersons())
	return source_objects


def initiate_face_detection(n_targets = 30, similarityThreshold = 70):
	global person_uid

	source_objects = get_sources()
	# Capture 30 targetFiles for face recognition
	face_detector.get_N_Face_Caps(n_targets)
	matched_object = find_perfect_match(source_objects, n_targets, similarityThreshold)

	person_uid = source_objects.index(matched_object)


def init():

	initiate_trash_type_detection()
	initiate_face_detection()
	db.addPersonPoint(person_uid)


if __name__ == "__main__":

	import register as reg
	binary_object = reg.take_picture()
	db.insertPerson("mississippi state", "ajinkya", "nawarkar", binary_object, 0)

	init()
