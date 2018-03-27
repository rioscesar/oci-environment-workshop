module "compartment_policies" {
  source = "./modules/cpolicies"
  name = "${var.compartment_name}"
  description = "${var.compartment_description}"
  tenancy_ocid = "${var.tenancy_ocid}"
  policy_name = "${var.policy_name}"
  policy_desc = "${var.policy_desc}"
}

# todo: the user makes the swift password just pass that in as a parameter
# will have to pass in different availability domains
module "object_storage" {
  source = "./modules/storage-swift"
  swift_description = "${var.swift_password_description}"
  user_id = "${var.user_ocid}"
  bucket_name = "${var.bucket_name}"
  compartment_id = "${module.compartment_policies.compartment_ocid}"
}

module "vcn" {
  source = "./modules/vcn"
  tenancy_ocid = "${var.tenancy_ocid}"
  compartment_ocid = "${module.compartment_policies.compartment_ocid}"
  dns_vcn = "${var.dns_vcn}"
  vcn_display = "${var.vcn_display}"
}

module "compute" {
  source = "./modules/compute-instance"
  tenancy_ocid = "${var.tenancy_ocid}"
  compartment_ocid = "${module.compartment_policies.compartment_ocid}"
  ssh_public_key = "${var.ssh_public_key}"
  ssh_private_key = "${var.ssh_authorized_private_key}"
  instance_shape = "${var.instance_shape}"
  image_ocid = "${var.image_ocid}"
  subnet = "${module.vcn.subnet1_ocid}"
  name = "${var.compute_name}"
  label = "${var.compute_label}"
  availability_domain = "${module.vcn.subnet1_ad}"
}

module "database" {
  source = "./modules/database"
  tenancy_ocid = "${var.tenancy_ocid}"
  compartment_ocid = "${module.compartment_policies.compartment_ocid}"
  availability_domain = "${module.vcn.subnet1_ad}"
  SubnetOCID = "${module.vcn.subnet1_ocid}"
  ssh_public_key = "${var.ssh_public_key}"
  DBNodeDomainName = "${module.vcn.subnet1_label}.${var.dns_vcn}.${var.oraclevcn}"
  DataStorgePercent = "${var.DataStorgePercent}"
  DBNodeShape = "${var.DBNodeShape}"
  CPUCoreCount = "${var.CPUCoreCount}"
  DBEdition = "${var.DBEdition}"
  DBAdminPassword = "${var.DBAdminPassword}"
  DBName = "${var.DBName}"
  DBVersion = "${var.DBVersion}"
  DBDisplayName = "${var.DBDisplayName}"
  DBDiskRedundancy = "${var.DBDiskRedundancy}"
  DBNodeDisplayName = "${var.DBNodeDisplayName}"
  DBNodeHostName = "${var.DBNodeHostName}"
  BastionHost = "${var.BastionHost}"
  HostUserName = "${var.HostUserName}"
  NCharacterSet = "${var.NCharacterSet}"
  CharacterSet = "${var.CharacterSet}"
  DBWorkload = "${var.DBWorkload}"
  PDBName = "${var.PDBName}"
  DataStorageSizeInGB = "${var.DataStorageSizeInGB}"
  LicenseModel = "${var.LicenseModel}"
  NodeCount = "${var.NodeCount}"
}

module "app-config" {
  source = "./modules/app-config"
  tenancy_ocid = "${var.tenancy_ocid}"
  compartment_ocid = "${module.compartment_policies.compartment_ocid}"
  public-ip = "${module.compute.public-ip}"
  ssh_private_key = "${var.ssh_authorized_private_key}"
}

module "paas" {
  source = "./modules/paas-config"
  user = "${var.user}"
  domain = "${var.domain}"
  password = "${var.password}"
}

output "Compute Public IP" {
  value = "${module.compute.public-ip}"
}

# output "DB Public IP" {
#   value = "${module.database.DBNodePublicIP}"
# }			

