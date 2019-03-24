#!/usr/bin/env python3

import trash_gcp_detector as trash_detector

if __name__ == "__main__":

	for i in range(3):
		sourceFile='../assets/test/opencv' + str(i) + '.jpg'
		print(trash_detector.init(sourceFile))
