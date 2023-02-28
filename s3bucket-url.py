import boto3
import re
s3 = boto3.client("s3",
                  region_name='REGION_NAME',
                  aws_access_key_id='AWS_ACCESS_KEY',       
                  aws_secret_access_key='AWS_SECRET')

bucket_response = s3.list_buckets()
all_objects = s3.list_objects(Bucket = 'BUCKET')                  

for i in all_objects['Contents']:
    #string manipulation
    title = 'APP '+ re.sub(r'^.*?APP', '', i['Key'])[1:-4] 
    url ='https://'+BUCKET+'.s3.'+REGION_NAME+'.amazonaws.com/'+ i['Key'].replace(" ", "+")
    print('{ title: "'+title+'",'+'url: "'+ url+'"},')
