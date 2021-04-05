import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.applications import MobileNetV2
import numpy as np
import time
import os
import json
def lambda_handler(event, context):
    # TODO implement
    model = MobileNetV2(weights='mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5')
    img_path = os.path.abspath('n03417042_11.JPEG')
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    cur = time.time()
    preds = model.predict(x)
    return {
        'statusCode': 200,
        'body': json.dumps(str(time.time()-cur))
    }
print(lambda_handler(1,2))