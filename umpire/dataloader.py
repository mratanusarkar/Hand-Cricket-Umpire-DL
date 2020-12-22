import tensorflow as tf


class DataLoader:

    def __init__(self, root_dir):
        self.root_directory = root_dir
        self.batch_size = None
        self.image_size = None

    def get_dataset_from_directory(self, batch_size, image_size):
        self.batch_size = batch_size
        self.image_size = image_size
        directory_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            directory=self.root_directory,
            image_size=(self.image_size, self.image_size),
            batch_size=self.batch_size
        )
        directory_dataset = directory_dataset.prefetch(buffer_size=32)
        return directory_dataset
