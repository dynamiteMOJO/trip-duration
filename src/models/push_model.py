import shutil
from upload_to_gcp_bucket import upload_blob

local_model_path = 'models/model.joblib'
gcp_bucket_name = 'test_ti_bucket'
gcp_file_path = 'prediction-testing-v1/models/model.joblib'

upload_blob(gcp_bucket_name, local_model_path, gcp_file_path)
shutil.copy(local_model_path, 'model.joblib')