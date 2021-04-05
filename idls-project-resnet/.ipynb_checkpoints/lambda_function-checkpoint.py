import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.applications import InceptionV3
import numpy as np
import time
import os
import json
def lambda_handler(event, context):
    # TODO implement
    model = InceptionV3(weights='resnet50_weights_tf_dim_ordering_tf_kernels.h5')
    img_path = os.path.abspath('n03417042_11.JPEG')
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    cur = time.time()
    preds = model.predict(x)
    return {
        'statusCode': 200,
        'body': json.dumps(str(time.time()-cur))
    }