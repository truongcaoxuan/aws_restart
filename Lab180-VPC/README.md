# Lab - Configure VPC
## Lab Overview
Traditional networking is hard — it involves equipment, cabling, complex configurations and specialist skills. Fortunately, Amazon VPC hides the complexity while making it easy to deploy secure private networks.

This lab shows you how to build your own Virtual Private Cloud and deploy resources.

The lab will demonstrate how to:

- Create a Virtual Private Cloud (VPC) that contains a private and public subnet, an Internet Gateway (IGW), and a Network Translation (NAT) Gateway.
- Configure Route Tables associated with a public subnet for internet-bound traffic to be directed to the IGW for direct internet access.
- Configure Route Tables associated with a private subnet for isolated resources to securely connect to the internet through a NAT Gateway.
- Launch a Bastion Host in a public subnet for resource-based secured access to the private subnet.
- Evaluate the operation of the private subnet's ability to communicate with the internet.

![architecture-lab-vpc](architecture-lab-vpc.png)
