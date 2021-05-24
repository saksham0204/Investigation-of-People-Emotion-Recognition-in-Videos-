import tensorflow
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import load_model
from tensorflow.python.ops.confusion_matrix import confusion_matrix

classifier = load_model(r'C:\Users\HP\PycharmProjects\hand gesture\venv\Emotion_little_vggg.h5')

