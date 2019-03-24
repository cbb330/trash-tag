#!/usr/bin/env python3

import trash_gcp_detector as trash_detector
import face_comparer_aws as face_comparer
from db import Database

##### TODO: Call opencv function to store trashimage
trashFilePath = '../assets/trash_image/trash_image.jpg'
trash_type = trash_detector.init(trashFilePath)

list_sources = [] ########## Db API function call to get all source images for all users

# Initialize forward variables
similarityThreshold = 70
n_targets = 30
targetFileDir = '../assets/target_images/'
##### TODO: Call opencv function to store target images


def find_perfect_match(sources, similarityThreshold):
	matched_sources = []

	if (len(sources) != 0):
		# Start comparing a source with all targets 
		for target_index in range(n_targets):

			# Extract the targetFile's binary object
			targetFilePath = targetFileDir + str(target_index) + '.jpg'
			targetFile = open(targetFilePath,'rb')

			# Find all sources that have match_confidence levels above current threshold
			for source_index in range(len(sources)):
				sourceFile = sources[source_index][2] ######## TODO: Get the binary object for source image	
				match_confidence = face_comparer.get_face_comparison_confidence(sourceFile, targetFile, similarityThreshold)
				if (match_confidence >= similarityThreshold):
					matched_sources.append(sources[source_index][2])

			# Check if we have found the perfect_match, return it
			if (len(matched_sources == 1)):
				return matched_sources[0]
			# Otherwise repeat for all the matched sources
			else:
				find_perfect_match(matched_sources, similarityThreshold+5)



find_perfect_match(list_sources, similarityThreshold)
###### TODO: Add point for the person in the Database
db = Database()
# db.insertItem(trash_type)


