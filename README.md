# Multiclass Classification Using Keras

### Setup

* Create a virtualenv (following commands use virtualenvwrapper)

```
mkvirtualenv neural
```

* Install requirements

```
pip install -r requirements.txt
```

### Raw data

The following data are being used in the example

* Images of celebs which can be downloaded from: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
* Images of flags downloaded from Wikipedia

### Project structure

root
  |
  raw_data
    |
    celebs
    flags
    test
      |
      afghanistan
      bangladesh
      china
      ...
    train
      |
      afghanistan
      bangladesh
      china
      ...
    validation
      |
      afghanistan
      bangladesh
      china
      ...
  create_dataset.py
  neural.py


### How to

#### Prepare data

* We can create the dataset for training, validation and testing using the **create_dataset.py** script
* Add the number of images required like the following

```
...
# Move required files to /train/<country> directory
prep_data(
    src=celebs_dataset,
    dst=train_data_dir,
    no_of_images_req=320)  # Creates 320 training images per class

# Move required files to /validation/<country> directory
prep_data(
    src=celebs_dataset,
    dst=validation_data_dir,
    no_of_images_req=240)  # Creates 240 validation images per class

# Move required files to /test/<country> directory
prep_data(
    src=celebs_dataset,
    dst=test_data_dir,
    no_of_images_req=100)  # Creates 100 testing images per class
```

* Run the training model

```
python neural.py train
```

* Predict image using

```
python neural.py predict path/to/an/image.jpg
```
