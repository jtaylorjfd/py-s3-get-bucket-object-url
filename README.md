# py-s3-get-bucket-object-url

Using the python Boto3 library to get S3 bucket title and object URL and translates into a JSON format

## Installation

Assuming you have Python3 and pip. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install boto3.

```bash
pip install boto3
```

The library re is optional for string manipulation.

### Run it locally

- Clone the new repository: `https://github.com/jtaylorjfd/py-s3-get-bucket-object-url.git`
- Input the AWS S3 variables `BUCKET`,`AWS_ACCESS_KEY_ID`,`AWS_SECRET_ACCESS_KEY_ID`,`REGION_NAME`. These can be found on [IAM](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users) and [S3 Buckets](https://s3.console.aws.amazon.com/s3/buckets/)
- To compile the script, run `python3 py-s3-get-bucket-object-url` in the terminal.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
