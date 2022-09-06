### Find all instances in your account that are tagged with a tag of Project and a value of ERPSystem:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem"
```
The command should output the full set of parameters available for all seven instances that are tagged Project=ERPSystem. 

### Use the --query parameter to limit the output of the previous command to only the instance ID of the discovered instance:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].InstanceId'
```
Your output entries will now consist of a list of instance IDs:
```
[ 
[
"i-135b491e" 
], 
[ 
"i-3e584a33" 
], 
… 
]
```
### To include both the instance ID and the Availability Zone of each instance in your return result:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```

### To include the value of the Project tag in your output:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value}'
```
Your output now includes the value of the Project tag:
```
[[{ 
"Project": "ERPSystem", 
"AZ": "us-west-2a", 
"ID": "i-3250b838" 
}],
…
]
```
#### The value of a specific named tag can be retrieved via a JMESPath query, using the following syntax:
```
Tags[?Key==\`Project\`] | [0].Value
```

### to also include the Environment and Version tags in your output:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```
The results will give you a fuller picture of the instances currently associated with the project named ERPSystem:
```
[[{ 
"Environment": "production", 
"Project": "ERPSystem", 
"Version": "1.0", 
"AZ": "us-west-2a", 
"ID": "i-3250b838" 
}], 
… 
]
```
### Finally, add a second tag filter to see only the instances associated with the project named ERPSystem that belong to the Environment named development:
```
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" \
--query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```
You should see only two instances returned by this command, both with a Project tag value of ERPSystem and an Environment tag value of development:
```
[[{ 
"Environment": "development", 
"Project": "ERPSystem", 
"Version": "1.0", 
"AZ": "us-west-2a", 
"ID": "i-9552ba9f" 
}], 
… 
]
```

