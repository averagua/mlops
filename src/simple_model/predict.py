from google.cloud import storage

storage_client = storage.Client()
model_path = 'mockup-model.dat'
model = model_bucket.get_blob(model_path).download_to_filename('model.dat')
print(model)
print(dir(model))
