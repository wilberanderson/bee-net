# Bee detection utility

## Automatic cropping

### Setup directory

0. Clone repository

    git clone github.com/wilberanderson/beeXXXXXXXXXXXX
    cd beeXXXXXXXXXX

1. Download the beespotter dataset: run `beescrape.py` until it all images are downloaded (roughly 15,000).

    python beescrape.py

2. Remove any images that are errored or have issues. This is kind of difficult, the easiest way to get a bunch out is to sort by file size and remove any that are zero bytes. There may be a few more with issues but you should be able to catch those during training as the scripts are written to give warnings for image issues.

### Choose training method

The way I set up my training sets during this phase was by using [roboflow](app.roboflow.ai). This works well when there isn't much data, but after a certain size you have to pay for more source images.

To follow my exact steps and replicate my procedure, copy ALL of the `.txt` files in `training_set_labels/seed_labels` into an empty directory. Then copy the images with the same names as those text files into the same directory. This is trivial and left as an exercise for the reader. Then upload the entire dataset to roboflow. My settings were:
    auto-orient: on
    resize: 416x416

    flip: horizontal
    90 degree rotates: clockwise, ccw, upside-down
    noise: <2% of pixels

Then export the data from roboflow as yolov5 labels. After each training and analysis phase, copy the most recent `label_data_*` folder to roboflow. Then update the second cell of the jupyter notebook with the download line that roboflow generates, adding the -o flag after the `unzip` command. The line should look something like this:

    !curl -L "https://app.roboflow.ai/ds/XXXXXXXXX?key=XXXXXXXXXX" > roboflow.zip; unzip -o roboflow.zip; rm roboflow.zip

### Running the notebook



### Dependencies

A bunch, mostly they should be covered when installing yolo at the beginning of `Training.ipynb`.