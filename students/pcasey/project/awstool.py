#!/usr/bin/env python3

""" AWS Configuration Tool by Paul Casey

This program is a menu-driven AWS utility that performs the following:

- Create, list, and delete subnets in the VPC
- Create, list, and delete S3 buckets. Also list the files in the buckets
- Create, list, and rename EC2 instances
- Start, stop, and terminate EC2 instances

"""

# Import Modules

import boto3
# import pprint
import sys
# import json

# Set the "resource" and "client" variables for EC2 and S3
# AWS functions are separated between the "client" and "resource"
# variables.

region = "us-west-2"
myvpc = "vpc-8089aee4"
mysg = "sg-3b319442"

ec2 = boto3.resource("ec2", region_name=region)
ec2c = boto3.client("ec2", region_name=region)
s3 = boto3.resource("s3", region_name=region)
s3c = boto3.client("s3", region_name=region)

# Insert your VPC ID on this line

vpc = ec2.Vpc(myvpc)

# Help menu

intro = """
AWS Configuration Tool by Paul Casey

Type 'csub' to create a subnet
Type 'dsub' to delete a subnet
Type 'lsub' to list the subnets
Type 'imake' to create an instance
Type 'istart' to start an instance
Type 'istop' to stop an instance
Type 'iterm' to terminate an instance
Type 'ilist' to list the instances
Type 'iren' to rename an instance
Type 'cbuck' to create an S3 bucket
Type 'dbuck' to delete an S3 buckets
Type 'lbuck' to list the S3 buckets
Type 'ls' to list all S3 files
Type 'x' to exit

"""


# Main prompt


def action_prompt():
    action = input("==> ")
    return action.strip()


# Print help menu

def help_menu():
    print(intro)

# Create VPC subnet function


def create_subnet():
    subnetvar = input("Enter the subnet: ").strip()
    az = input("Enter the availability zone: ").strip()

    try:
        newsub = vpc.create_subnet(CidrBlock=subnetvar, AvailabilityZone=az)
        print("\nThe subnet ID created was {}".format(newsub.id))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# Delete VPC subnet function


def delete_subnet():
    subid = input("Enter the subnet ID: ").strip()

    try:
        ec2c.delete_subnet(SubnetId=subid)
        print("\nThe subnet {} was deleted.".format(subid))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))


# List VPC subnets function


def list_subnets():
    listsub = ec2c.describe_subnets()

    for sub in listsub["Subnets"]:
        print("Subnet ID = {0} with CIDR of {1} in AZ {2} with {3} available IPs".format(sub["SubnetId"], sub["CidrBlock"], sub["AvailabilityZone"], str(sub["AvailableIpAddressCount"])))
    return(listsub)

# Create new EC2 instances function


def create_inst():
    subid = input("Enter the subnet ID: ").strip()
    instname = input("Enter the name: ").strip()

    try:
        newinst = ec2.create_instances(ImageId="ami-b04e92d0", MinCount=1, MaxCount=1, InstanceType="t2.micro", SecurityGroupIds=[mysg], SubnetId=subid)
        ec2c.create_tags(Resources=[newinst[0].id], Tags=[{"Key": "Name", "Value": instname}])
        print("\nThe instance ID created was {} and is named {}".format(newinst[0].id, instname))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# Start and stop EC2 instances functions


def start_inst():
    instid = input("Enter the instance ID: ").strip()

    try:
        ec2c.start_instances(InstanceIds=[instid])
        print("Started instance {}".format(instid))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))


def stop_inst():
    instid = input("Enter the instance ID: ").strip()

    try:
        ec2c.stop_instances(InstanceIds=[instid])
        print("Stopped instance {}".format(instid))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# Terminate EC2 instances function


def term_inst():
    instid = input("Enter the instance ID: ").strip()

    try:
        ec2c.terminate_instances(InstanceIds=[instid])
        print("Terminated instance {}".format(instid))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))


# List EC2 instances function


def list_inst():
    listinst = ec2.instances.all()
    for i in listinst:
        print("ID: {0}  Name: {1}  Type: {2}  State: {3}".format(i.id, i.tags[0]["Value"], i.instance_type, i.state["Name"]))
    return(listinst)

# Rename an EC2 instance function


def ren_inst():
    instid = input("Enter the instance ID: ").strip()
    newname = input("Enter the new name: ").strip()

    try:
        ec2c.create_tags(Resources=[instid], Tags=[{"Key": "Name", "Value": newname}])
        print("The instance was renamed to {}".format(newname))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# Create S3 bucket function


def create_bucket():
    buckname = input("Enter the bucket name: ").strip()

    try:
        newbuck = s3c.create_bucket(Bucket=buckname)
        print("\nBucket {} was created successfully.".format(newbuck["Location"]))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# Delete S3 bucket function


def delete_bucket():
    buckname = input("Enter the bucket name: ").strip()

    try:
        s3c.delete_bucket(Bucket=buckname)
        print("Bucket {} was deleted successfully.".format(buckname))
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))

# List S3 buckets function


def list_buckets():
    listbuck = s3.buckets.all()
    print("\nList of buckets:")
    for b in listbuck:
        print(b.name)
    return(listbuck)

# List S3 files function


def list_files():
    listfile = s3.buckets.all()
    for buck in listfile:
        for obj in buck.objects.all():
            print("Bucket: {0}  File: {1}".format(buck.name, obj.key))
    return(listfile)

# Quit function


def quit():
    sys.exit(0)


if __name__ == "__main__":

# Using dict as switch for calling menu items

    select_dict = {"csub": create_subnet,
                   "dsub": delete_subnet,
                   "lsub": list_subnets,
                   "imake": create_inst,
                   "istart": start_inst,
                   "istop": stop_inst,
                   "iterm": term_inst,
                   "ilist": list_inst,
                   "iren": ren_inst,
                   "cbuck": create_bucket,
                   "lbuck": list_buckets,
                   "dbuck": delete_bucket,
                   "ls": list_files,
                   "help": help_menu,
                   "x": quit,
                   "exit": quit,
                   "quit": quit,
                   "q": quit,
                   }

# Print help menu

    help_menu()

# Action prompt routine
    while True:
        selection = action_prompt()
        try:
            select_dict[selection]()
        except KeyError:
            print("Invalid selection. Type 'help' for a list of commands")
