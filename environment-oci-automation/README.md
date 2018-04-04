# OCI Terraform Environment Automation 

#### *Disclaimer! This is not production level code. Should be treated as a resource/workshop on how to connect different technologies with OCI using Terraform.*

## Modify the env.sh file to match your configurations to point to your cloud environment. 

`
###################### Environment Setup  ####################################
#Enter Your Tenancy OCID
export TF_VAR_tenancy_ocid="ocid1.tenancy.oc1..xxxxxxxxxx"
#Enter Your User OCID
export TF_VAR_user_ocid="ocid1.user.oc1..xxxxxxx"
#Enter Your Fingerprint
export TF_VAR_fingerprint="fb:93:b0:6c:ac:f2:42:xxxxxxx"
#Enter Your Region
export TF_VAR_region="us-ashburn-1"

#Enter Your Username
export TF_VAR_user="cloud.admin"
#Enter Your Password 
export TF_VAR_password="XXXX@0XXXX"
#Enter the IDCS ID of your domain
export TF_VAR_domain="idcs-xxxxxx"
#Enter Identity Domain tenancy name
export TF_VAR_tenancy="gsexxxx"
#Enter Object Storage Container user
export TF_VAR_object_storage_user="gse-adminxxx@xxx.com"

#Change following fields to point to correct keys
#Enter private SSH key's path 
export TF_VAR_private_key_path="userdata/APIkey.pem"
#Enter public SSH key's path
export TF_VAR_ssh_public_key_path="userdata/test_ssh.pub"
export TF_VAR_ssh_public_key=$(cat userdata/test_ssh.pub)
export TF_VAR_ssh_authorized_private_key=$(cat userdata/test_ssh)`


From link "https://github.com/rioscesar/oci-environment-workshop/tree/master/environment-oci-automation/installer/OracleWebLogic/dockerfiles/12.2.1" download fmw_12.2.1.0.0_wls_Disk1_1of1.zip.download and fmw_12.2.1.0.0_wls_quick_Disk1_1of1.zip.download and insert into directory.

From link "https://github.com/rioscesar/oci-environment-workshop/tree/master/environment-oci-automation/installer/OracleJava/java-8" download "server-jre-8u161-linux-x64.tar.gz" and insert into directory.
  
## Missing directories:
  * userdata

#### The userdata directory contains your APIkey.pem (logs you into your cloud account) as well as your public and private ssh keys you will use to log into your newly created instances. If you need help creating either of these take a look at Oracle's documentation: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm.
  * Create the APIkey.pem file. 
  * Don't forget to also add your private and public ssh keys into the userdata directory.

##### terraform plan -out=plan.out
##### terraform apply "plan.out"

#### DESTROY EVERYTHING!

##### terraform destroy 
