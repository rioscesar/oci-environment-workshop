# OCI Terraform Environment Automation 

#### *Disclaimer! This is not production level code. Should be treated as a resource/workshop on how to connect different technologies with OCI using Terraform.*

## Modify the env.sh file to match your configurations to point to your cloud environment. 


###################### Environment Setup  ####################################3
```
#Enter Your Tenancy OCID
export TF_VAR_tenancy_ocid="ocid1.tenancy.oc1..aaaaaaaaugd5a3u46fepw7omxhjlx6rs24onw3j4gnvcndtglk6hy4ura7nq"
#Enter Your User OCID
export TF_VAR_user_ocid="ocid1.user.oc1..aaaaaaaanfjhntw3gum43ucmsvaokwlr7bpex6stodttp4tsmzyvayrsjasq"
#Enter Your Fingerprint
export TF_VAR_fingerprint="fb:93:b0:6c:ac:f2:42:c7:97:00:43:82:f3:27:97:91"
#Enter Your Region
export TF_VAR_region="us-ashburn-1"

#Enter Your Username
export TF_VAR_user="cloud.admin"
#Enter Your Password 
export TF_VAR_password="InbOrn@0BLOw"
#Enter the IDCS ID of your domain
export TF_VAR_domain="idcs-d0b3ef5f88954f9fb37302f2149f2416"
#Enter Identity Domain tenancy name
export TF_VAR_tenancy="gse00013851"
#Enter Object Storage Container user
export TF_VAR_object_storage_user="gse-admin_ww@oracle.com"
# todo: this needs to be manually configured before
#Enter swift password of the user
#export TF_VAR_object_swift_password=""

#Change following fields to point to correct keys
#Enter private SSH key's path 
export TF_VAR_private_key_path="userdata/APIkey.pem"
#Enter public SSH key's path
export TF_VAR_ssh_public_key_path="userdata/test_ssh.pub"
export TF_VAR_ssh_public_key=$(cat userdata/test_ssh.pub)
export TF_VAR_ssh_authorized_private_key=$(cat userdata/test_ssh)
```
  
## Missing directories:
  * userdata

#### The userdata directory contains your APIkey.pem (logs you into your cloud account) as well as your public and private ssh keys you will use to log into your newly created instances. If you need help creating either of these take a look at Oracle's documentation: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm.
  * Create the APIkey.pem file. 
  * Don't forget to also add your private and public ssh keys into the userdata directory.

##### terraform plan -out=plan.out
##### terraform apply "plan.out"

#### DESTROY EVERYTHING!

##### terraform destroy 
