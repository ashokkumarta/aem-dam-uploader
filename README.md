# aem-dam-uploader							
Script to upload all the assets under a specified local folder to AEM, preserving the same folder structure in AEM as in the local 

## Dependencies
```
Python 3.7
```

## Usage

Update the configuration in the json file config/config.json and run the upload script 
```
python scripts/asset-upload.py
```

### Folder structure
```
scripts - contains the script and dependent libraries for this upload utility
config - Has a single json configuration file - config.json which holds all the configuration for the upload
upload - default source folder. This folder contains the assets to upload
output - outputs folder. This folder contains the output files  
logs - log files folder. This folder has all the logs generated
```

###Configuration to change in config.json
```
cq_host - Host name of the AEM instance to connect to 
cq_port - Port number of the AEM instance
cq_user - User ID to connect to the AEM Instance	
cq_password - Password of the AEM User ID
source_dir - Local path from which assets needs to be uploaded
time_wait_secs - Time delay in secs between each upload 
```

###Output files
```
output/successful_assets.lst - List of assets which are uploaded successfully
output/failed_assets.lst - List of assets for which upload failed
```

###How to run
Before starting the batch run, ensure
+ Correct configurations are done in the config.json file 
+ upload, output and log folders containing data if any from previous run are backed up (if needed) and contents of these folders cleared.  

After the above points are checked, run the script scripts/asset-upload.py by executing the below command 
```
python scripts/asset-upload.py 
```

###Checking the status of the run
The progress and the status summary of the migration run is displayed on the console. 
Detailed logging is also done to check and validate the migration. 
The following log files can be referred for debugging
+ logs/status.log - Overall summary of the migration run
+ logs/trace.log - Detaied track on the migration run, including the details of the assets upload status
+ logs/error.log - Error details about the migration failures
The following output files can be checked to find the details of the assets uploaded vs. failed
+ output/successful_assets.lst - List of assets which are uploaded successfully
+ output/failed_assets.lst - List of assets for which upload failed

## Reservation
> These scripts are created for specific use cases. Make sure its tested for your scenario before applying it for production purpose

---
> Environment Tested on:  AEM 6.1, 6.2 & 6.4 | Windows, RHEL5 | Python 3.7.2

