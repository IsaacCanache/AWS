import boto3

client = boto3.client('dynamodb', region_name='us-east-2')

  
resp = client.create_table( 
    TableName="Books", 
    KeySchema=[ 
        {"AttributeName": "Author","KeyType": "HASH"}, 
        {"AttributeName": "Title","KeyType": "RANGE"} 
    ],
    AttributeDefinitions=[ 
       {"AttributeName": "Author","AttributeType": "S"}, 
       {"AttributeName": "Title","AttributeType": "S"} 
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1})