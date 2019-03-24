# trash-tag

1. Add credentials to virtualenv/activate and init local test db using GCP cli
  https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test
  
2. Use ```pip install --upgrade google-cloud-vision``` to install google cloud vision client libraries.

3. Use below to add Google API credentials to activate cloud requests
  ```console
  echo 'export GOOGLE_APPLICATION_CREDENTIALS=./key.json' >> ~/.bashrc
  source ~/.bashrc
  ```

4. [Install boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation) and configure IMA user account using AWS CLI to start facial recognition API. 
 
4. Use ```./runner.py``` script to start serving detection and scoring system after giving it executable permissions 


4. Install opencv
