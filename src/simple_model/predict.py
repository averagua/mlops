from google.cloud import storage
import logging

try:
    storage_client = storage.Client()
    model_path = 'mockup-model.dat'
    model = model_bucket.get_blob(model_path).download_to_filename('model.dat')
    print(model)
    print(dir(model))
except Exception as e:
    logging.info(e)
