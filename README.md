

# 

virtualenv -p python3 dev/
source dev/bin/activate
pip install -r requirements.txt

# aws sqs : commands
aws --endpoint-url=http://localstack:4566 sqs create-queue --queue-name my_queue
aws --endpoint-url=http://localstack:4566 sqs purge-queue --queue-url http://localstack:4566/000000000000/my_queue 
aws --endpoint-url=http://localstack:4566 sqs send-message --queue-url http://localstack:4566/000000000000/my_queue --message-body "{\"s3\":{\"bucket\":\"selenium-tests\",\"object\":\"my_test.py\"}}"

# aws s3 : commnads
aws --endpoint-url=http://localstack:4566  s3api create-bucket --bucket selenium-tests --region eu-west-3
aws --endpoint-url=http://localstack:4566 s3 ls
aws --endpoint-url=http://localstack:4566 s3 cp samples/my_test.py s3://selenium-tests
aws --endpoint-url=http://localstack:4566 s3 cp s3://selenium-tests/my_test.py my_test.py