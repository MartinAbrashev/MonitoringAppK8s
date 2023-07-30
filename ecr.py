import boto3    
# used to create aws resources to the cloud 

ecr_client = boto3.client('ecr') 
#ecr client

repository_name = "abro-repo"   
# define repo name, 
response = ecr_client.create_repository(repositoryName=repository_name) 

# call the create_repository function, use create_repository API, use data 
# ----------- (repositoryName=%%%%%%%) 

repository_uri = response['repository']['repositoryUri']
# repository_uri will store the value of the response 

print(repository_uri)





