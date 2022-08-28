# Configure the AWS CLI
## Discover the region in which the Command Host instance is running:
```
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
```
## Update the AWS CLI software with the credentials.
```
aws configure
```
- AWS Access Key ID: Press enter.
- AWS Secret Access Key: Press enter.
- Default region name: Type in the name of the region, which you just discovered a moment ago. For example, us-east-1 or eu-west-2.
- Default output format: json

Copy and paste the following into ~/.aws/credentials
```
[default]
aws_access_key_id=ASIAXVVMNAWFHL25ZMVO
aws_secret_access_key=qac0T/ncqEuxTlUBdtJQ7iqw6NYiLKwcIRnSDbhu
aws_session_token=FwoGZXIvYXdzEJr//////////wEaDKzih6P4/eIVDSCvAiLEAfsOQE7BtQt1YOQi2jJtntc0/6YlQLe8RpYak05vQdn51euGKHrJHBfMlUD7ZXDbc2Um0cLukx51RoLCn+pvc5lp4NkWiRrGIMTMcQ8RTq9OgFN9ZmEvMScMT8uo1f3ttyM73jkZfBc3DYD90OM//I+03wq9afU31nnkqepPSQQ1OEWkQ4gFlADUSmQNETQ0GF8EKL2DD8P9S2Qto4YV0G22JMYvApwL0F07bmCcGYHIChds9xOR7xIvfax+Y3iormjbVf0o3MasmAYyLXoePudPnZ1u7KbKQETyMXPbATIGLyK5Ug1WRELf3tALqYWT1uR61jiHoW9DlA==
```

# Create A New EC2 Instance
```
more UserData.txt
```
```
#!/bin/bash
yum update -y --security
amazon-linux-extras install epel -y
yum -y install httpd php stress
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
wget http://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-TULABS-1/10-lab-auto
scaling-linux/s3/ec2-stress.zip
unzip ec2-stress.zip

echo 'UserData has been successfully executed. ' >> /home/ec2-user/result
find -wholename /root/.*history -wholename /home/*/.*history -exec rm -f {} \;
find / -name 'authorized_keys' -exec rm -f {} \;
rm -rf /var/lib/cloud/data/scripts/*
```

- AMIID=ami-07d59d159373b8030
- HTTPACCESS=sg-003a05e6c07b84188
- COMMANDHOSTIP	52.41.136.5
- KEYNAME=vockey
- SUBNETID=subnet-09bbf8589b5ba0372


```
aws ec2 run-instances \
--key-name vockey \
--instance-type t3.micro \
--image-id ami-07d59d159373b8030 \
--user-data file:///home/ec2-user/UserData.txt \
--security-group-ids sg-003a05e6c07b84188 \
--subnet-id subnet-09bbf8589b5ba0372 \
--associate-public-ip-address \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServerBaseImage}]' \
--output text \
--query 'Instances[*].InstanceId'
```
instanceId: i-000f025bcc5da7027

# Use the aws ec2 wait instance-running command to monitor this instance's status
```
aws ec2 wait instance-running --instance-ids i-000f025bcc5da7027
```
# Obtain the public DNS name
```
aws ec2 describe-instances \
--instance-id i-000f025bcc5da7027 \
--query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
```
* Public-dns-address :: ec2-35-91-82-108.us-west-2.compute.amazonaws.com
* http://ec2-35-91-82-108.us-west-2.compute.amazonaws.com/index.php

# Create a Custom AMI

```
aws ec2 create-image \
--name WebServer \
--instance-id i-000f025bcc5da7027
```
"ImageId": "ami-0c421515067b7f9ac"

webserverloadbalancer-1179626913.us-west-2.elb.amazonaws.com
