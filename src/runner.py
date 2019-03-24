#!/usr/bin/env python3

import trash_gcp_detector as trash_detector
from db import Database

trash_type = trash_detector.init()

db = Database()
db.insertItem(trash_type)