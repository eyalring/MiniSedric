Mini Sedric is a tool which can be used to transcribe audio files to text. It uses AWS Transcribe service to transcribe the audio files.

In order to run the test you need to have a mp3 audio file in accessible bucket in Amazon s3. 
Use the following link to access and upload a file to s3 bucket. [Amazon S3](https://aws.amazon.com/s3/)

In order to start up the server you need to run the main.py file under the src directory. You will have to add to the env vars the authentication for accessing the AWS transcribe service. 
For example :
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export REGION_NAME=your_region

python ./src/main.py
```


Once you have the file in s3 bucket, you can run the test by running an API call.
Example for running the API using curl :


```bash
curl --location --request GET 'localhost:56078' \
--header 'Authorization: Basic test' \
--header 'Content-Type: application/json' \
--data '{
    "interaction_url": "s3://eyalsongsbuket2/RIP Coyote Condo #5.mp3",
    "trackers": [
        "Quite certai",
        "value2"
    ]
}'
```

The above command will run the test on the audio file "RIP Coyote Condo #5.mp3" and will check if the audio file contains the trackers "Quite certai" and "value2". Trackers are regex patterns which can be searched in the audio file transcript.


planned testing : 
1. Test the API with different audio files.
2. Test the API with different trackers.
3. Test the API with no file in bucket.
4. Test the API with no trackers.
5. Test the API with invalid file path.
6. Test the API with invalid regex in tracker.

unit tests : for each file test the functionallity of the code.



missing - authorizations , error handling , logging , unit tests , moving to core directory , authentication to use cloud secrets

