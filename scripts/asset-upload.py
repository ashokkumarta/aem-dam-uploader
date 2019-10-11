import os, requests, json, time
from datetime import datetime
from log_util import * 

def load_config():
    config_file = 'config/config.json'
    config=open(config_file).read()
    return json.loads(config)

def getTargetPath(asset):
    target_full_path = config_json['path_to_download'] + asset
    return os.path.dirname(target_full_path), os.path.basename(target_full_path)

def logStatus(msg):
    s_log.info(msg)
    print (msg)

def get_timestamp():
    return datetime.now().strftime('%d %b %Y, %H:%M:%S')

# Start 
s_time = get_timestamp()


#Load config
config_json = load_config()

# Initialize loggers
t_log = get_logger(config_json['trace_log'])
e_log = get_logger(config_json['error_log'])
s_log = get_output_handler(config_json['status_log'])

# Initialize output file handler (uses log library)
s_handle = get_output_handler(config_json['successful_assets'])
f_handle = get_output_handler(config_json['failed_assets'])

# Initialize variables
assets_to_upload = []
total = 0
failure = 0

try:

    for r, d, f in os.walk(config_json['source_dir']):
        for asset in f:
            t_log.info(r)
            t_log.info(asset)
            t_log.info(os.path.join(r, asset))
            assets_to_upload.append(os.path.join(r, asset))

                
except  Exception as e:
    e_log.error('Unexpected Error : '+str(e))


# Report status
logStatus("\nStatus:\n=======")
logStatus("Download start time : "+s_time)
logStatus("Download completion time : "+get_timestamp())
logStatus("Assets downloaded : "+str(total - (failure)))
if failure :
    logStatus("Download failed : "+str(failure))
    logStatus("Check the logs at "+config_json['error_log']+" for error details")

