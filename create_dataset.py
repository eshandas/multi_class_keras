import os
from shutil import copyfile

from random import randint

from PIL import Image

train_data_dir = '/home/yml/Documents/Stuff/flags/raw_data/train'
validation_data_dir = '/home/yml/Documents/Stuff/flags/raw_data/validation'
test_data_dir = '/home/yml/Documents/Stuff/flags/raw_data/test'
celebs_dataset = '/home/yml/Documents/Stuff/flags/raw_data/celebs'
flags_dataset = '/home/yml/Documents/Stuff/flags/raw_data/flags'

countries = [
    'india',
    'pakistan',
    'china',
    'sri_lanka',
    'myanmar',
    'bangladesh',
    'afghanistan']


# Create required folders in /train directory
for country in countries:
    directory = '%s/%s' % (train_data_dir, country)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create required folders in /validation directory
for country in countries:
    directory = '%s/%s' % (validation_data_dir, country)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create required folders in /test directory
for country in countries:
    directory = '%s/%s' % (test_data_dir, country)
    if not os.path.exists(directory):
        os.makedirs(directory)


def prep_data(src, dst, no_of_images_req):
    idx = 0
    # no_of_images_req -= 1
    for country in countries:
        # if country == 'pakistan':
        #     import ipdb; ipdb.set_trace()
        files = os.listdir(src)[idx:(idx + no_of_images_req)]
        for file in files:
            _src = '%s/%s' % (src, file)
            _dst = '%s/%s/%s' % (dst, country, file)
            copyfile(_src, _dst)

        # Create training dataset
        country_src = '%s/%s' % (dst, country)
        foreground = Image.open('%s/%s.png' % (flags_dataset, country))
        files = os.listdir(country_src)
        for file in files:
            background = Image.open('%s/%s' % (country_src, file))
            foreground.thumbnail((100, 100), Image.ANTIALIAS)

            paste_loc = (randint(0, background.size[0] - 100), randint(0, background.size[1] - 100))

            background.paste(foreground, paste_loc)
            background.save('%s/%s' % (country_src, file))

        idx += no_of_images_req


# Move required files to /train/<country> directory
prep_data(
    src=celebs_dataset,
    dst=train_data_dir,
    no_of_images_req=320)


# Move required files to /validation/<country> directory
prep_data(
    src=celebs_dataset,
    dst=validation_data_dir,
    no_of_images_req=240)


# Move required files to /test/<country> directory
prep_data(
    src=celebs_dataset,
    dst=test_data_dir,
    no_of_images_req=100)
