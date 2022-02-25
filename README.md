# Description
When data is sent to api gateway via application or postman, it is stored in s3 bucket. Athena is then used to query
files stored in s3

## Note
* Change value of **destination_bucket** in **lambda_function** with your s3 bucket name
* **SSN** should be present in every record else it throws error.

## Demo Video
* https://youtu.be/l4A5FxTuFcE
