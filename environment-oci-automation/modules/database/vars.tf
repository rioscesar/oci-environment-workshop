variable "compartment_ocid" {}
variable "ssh_public_key" {}
variable "tenancy_ocid" {}
variable "availability_domain" {}
variable "SubnetOCID" {}

# DBSystem specific 
variable "DataStorgePercent" {}
variable "DBNodeShape" {}
variable "CPUCoreCount" {}
variable "DBEdition" {}
variable "DBAdminPassword" {}
variable "DBName" {}
variable "DBVersion" {}
variable "DBDisplayName" {}
variable "DBDiskRedundancy" {}
variable "DBNodeDisplayName" {}
variable "DBNodeHostName" {}
variable "DBNodeDomainName" {}

# Define existing bastion host
variable "BastionHost" {}
variable "HostUserName" {}
variable "NCharacterSet" {}
variable "CharacterSet" {}
variable "DBWorkload" {}
variable "PDBName" {}
variable "DataStorageSizeInGB" {}
variable "LicenseModel" {}
variable "NodeCount" {}
