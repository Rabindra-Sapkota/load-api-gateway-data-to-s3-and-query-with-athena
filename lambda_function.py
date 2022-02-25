import json
import boto3


def lambda_handler(event, context):
    try:
        destination_bucket = 'user-data-project'
        user_data = event
        if 'SSN' not in user_data.keys():
            print('Error. Missing SSN Value. SSN is mandatory')
            return json.dumps({"Status": "Error", "Reason": "Missing SSN value"})

        print("Generating file name")
        file_name = str(user_data.get('SSN')) + '.json'
        s3_resource = boto3.resource('s3')

        print(f"Creating Object handler with Bucket: {destination_bucket}, file: {file_name}.")
        object_handler = s3_resource.Object(destination_bucket, file_name)

        print(f"Uploading file: {file_name} to bucket: {destination_bucket}")
        object_handler.put(Body=bytes(json.dumps(user_data), encoding='utf-8'))
        print(f"Successfully Uploaded file: {file_name} to bucket: {destination_bucket}")

        return json.dumps({"Status": "Success"})

    except Exception as e:
        print("Error Occur while processing data.")
        print(e)
        return json.dumps({"Status": "Error", "Reason": str(e)})
