# Terraform and Stack Manager oci-environment-workshop

#### *Disclaimer! This is not production level code. Should be treated as a resource/workshop on how to connect different technologies on OCI using Terraform.* 

### Modify the env.sh file to match your configurations to point to your cloud environment. This is a file you will add and run after doing `terraform init`. Run it as a regular shell script. `. env.sh` 
```
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
export TF_VAR_ssh_authorized_private_key=$(cat userdata/test_ssh)
```

From link "https://github.com/rioscesar/oci-environment-workshop/tree/master/environment-oci-automation/installer/OracleWebLogic/dockerfiles/12.2.1" download fmw_12.2.1.0.0_wls_Disk1_1of1.zip.download and fmw_12.2.1.0.0_wls_quick_Disk1_1of1.zip.download and insert into directory.

From link "https://github.com/rioscesar/oci-environment-workshop/tree/master/environment-oci-automation/installer/OracleJava/java-8" download "server-jre-8u161-linux-x64.tar.gz" and insert into directory.
  
## Missing directories:
  * userdata

#### The userdata directory contains your APIkey.pem (logs you into your cloud account) as well as your public and private ssh keys you will use to log into your newly created instances. If you need help creating either of these take a look at Oracle's documentation: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm.
  * Create the APIkey.pem file. 
  * Don't forget to also add your private and public ssh keys into the userdata directory.

#### After the Terraform finishes creating the infrastructure, you will have a SOACS, JCS, OCI Compute, and OCI Database Instance. Once everything is done the next steps are required: 
  * Go to the Liberty application, LibertyInsuranceBE.java and modify the dbIP and SID to point to the Application Database created by TF.
  * Go to WebContent/resources/js/config.json and modify compute_ip to point to the new OCI Compute IP. (This is done in order to connect the frontend with the backend)
  * Go back to the Terraform project and open ups the root vars.tf. Modify variable DeployInsuranceApp to be a "1". 
  * Deploy the application to a war file and move it to the apps folder in the Terraform project. 
  * Run `terraform apply`
  * The app should deploy to OCI WebLogic.
  
#### Configure and install the ServiceBus application using the documentation found on Documentation/SOA Deployment.docx

#### Now configure the JCS State application. 
  * Go to State Application, StateGov.java, and modify the proxyIP to point to the SOA app, the dbIP and SID to point to the Application Database. 
  * Go to WebContent/resources/js/config.json and modify compute_ip to point to the new OCI Compute IP. (This is done in order to connect the frontend with the backend)

## This step is not required if deploying to JCS without using the tunnel/t3 channel created using the WebLogic steps in the Documentation folder. 
  * Go back to the Terraform project and open ups the root vars.tf. Modify variable DeployStateApp to be a "1". 
  * Deploy the application to a war file and move it to the apps folder in the Terraform project. 
  * Run `terraform apply`
  * The app should deploy to JCS. 

#### After configuring Terraform follow the SOA steps in the Documentation folder and then follow the Weblogic steps and deployment of second application.  

##### terraform plan -out=plan.out
##### terraform apply "plan.out"

#### DESTROY EVERYTHING!

##### terraform destroy 
