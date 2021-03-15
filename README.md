# Simple-Lane-Line-Detection
This project is a simple Lane line detection algorithm made using elementary principles of image processing.

# Components of this project
1. The polygon roi selection algorithm that lets you select a polygonal ROI in an image as opposed to a rectangular ROI thats allowed in opencv.
2. The Lane Line detection algorithm : Uses thresholding and contours to detect lanes (nothing fnacy here). To localise the vehicle, you may find the centroid of the detected contours. This would imply that the vehicle is between the coordinates of the centroids (a little more to this but its not that hard to do).

# Control flow of the project files
1. Run the polygon_roi.py file to generate the coordinates of the ROI. This saves the coordinates in a .csv file called roi_lane.csv
2. Run the Lane line detection code file. This reads the .csv that was generated earlier and uses the coordinates for region masking and image processing.

## I have included a sample video and a sample .csv file in the repo. Note that you will have to change the paths to files in the code.

## Disclaimer
The video used in this project is not mine and I have no claims over it.
