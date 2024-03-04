import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# load the data
valid_data_dir = 'data/test'
train_data_dir = 'data/train'

# Define the image size and batch size
img_size = 224
batch_size = 32

# Create an instance of the ImageDataGenerator class for data augmentation
train_datagen = ImageDataGenerator(rescale=1./255,rotation_range=20,zoom_range=0.2,horizontal_flip=True)

# Create generators for the training and validation datasets
train_generator = train_datagen.flow_from_directory(train_data_dir,target_size=(img_size, img_size),batch_size=batch_size,class_mode='binary')
validation_generator = train_datagen.flow_from_directory(valid_data_dir,target_size=(img_size, img_size),batch_size=batch_size,class_mode='binary')

# Define the architecture of the model
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)), tf.keras.layers.MaxPooling2D((2, 2)),tf.keras.layers.Conv2D(64, (3, 3), activation='relu'), tf.keras.layers.MaxPooling2D((2, 2)), tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),tf.keras.layers.MaxPooling2D((2, 2)),tf.keras.layers.Flatten(), tf.keras.layers.Dense(128, activation='relu'),tf.keras.layers.Dropout(0.5),tf.keras.layers.Dense(1, activation='sigmoid')])

# Define the loss function and optimizer
loss_fn = tf.keras.losses.BinaryCrossentropy()
optimizer = tf.keras.optimizers.Adam()

# Compile the model
model.compile(optimizer=optimizer, loss=loss_fn, metrics= ['accuracy'])

# Train the model on the training set
model.fit(train_generator, steps_per_epoch=train_generator.samples//batch_size, epochs=10, validation_data=validation_generator, validation_steps=validation_generator.samples//batch_size)

# Save the trained model
model.save('model.h5')