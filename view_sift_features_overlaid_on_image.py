'''
Author:  Steve North
Author URI:  http://www.cs.nott.ac.uk/~pszsn/
License: AGPLv3 or later
License URI: http://www.gnu.org/licenses/agpl-3.0.en.html
Can: Commercial Use, Modify, Distribute, Place Warranty
Can't: Sublicence, Hold Liable
Must: Include Copyright, Include License, State Changes, Disclose Source

Copyright (c) 2016, The University of Nottingham
'''

from PIL import Image
from pylab import *
from vlfeat_interface import *

root_path = "./input_files"

for filename in os.listdir(root_path):
  if ".sift" in filename:
    features = filename
  if ".jpg" in filename:
    image = filename

l,d = read_features_from_file(root_path + "/" + features)
im = array(Image.open(root_path + "/" + image))
figure()
plot_features(im,l,True)
show()
