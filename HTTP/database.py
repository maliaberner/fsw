import boto3

def initalize_db():
    client = boto3.client('dynamodb')
    return client

def add_user(email, first_name, last_name)
    client = initalize_db()
    response = client.put_item(
        TableName = 'user_info'
        Item={
            "email":email,
            'first_name':first_name,
            'last_name':last_name
        }
    )

if __name__ == '__main__':
    add_user('malia@malia.com', 'Malia', 'Berner')
