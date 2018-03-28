resource "null_resource" "soa-manager" {
  provisioner "local-exec" {
    #command = "python stackmanager.py create soa -u cloud.admin -p StariNg@9Scent --debug -dn idcs-72b2b9f4472e4a80ab7e5e0c1e629688"
    #command = "python stackmanager.py create jcs -u cloud.admin -p StariNg@9Scent --debug -dn idcs-72b2b9f4472e4a80ab7e5e0c1e629688"
    command = "echo '{\"publicKeyText\":\"${join(" ",slice(split(" ",file("${var.ssh_public_key_path}")),0,2))}\", \"commonPwd\":\"${var.password}\", \"sRegion\":\"${var.region}\", \"availabilityDomain\":\"${var.availability_domain}\", \"backupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"dbBackupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"backupStorageUser\":\"${var.object_storage_user}\", \"backupStoragePassword\": \"${var.swift_password}\", \"subnet\":\"${var.subnet}\", \"dbComputeShape\":\"${var.DBShape}\", \"wlComputeShape\":\"${var.JCSShape}\", \"wlComputeShape2\":\"${var.JCSShape}\"}' > soa.json"
  }
}


resource "null_resource" "jcs-manager" {
  provisioner "local-exec" {
    command = "echo '{\"publicKeyText\":\"${join(" ",slice(split(" ",file("${var.ssh_public_key_path}")),0,2))}\", \"commonPwd\":\"${var.password}\", \"sRegion\":\"${var.region}\", \"availabilityDomain\":\"${var.availability_domain}\", \"dbBackupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"backupStorageUser\":\"${var.object_storage_user}\", \"backupStoragePassword\": \"${var.swift_password}\", \"subnet\":\"${var.subnet}\", \"dbComputeShape\":\"${var.DBShape}\", \"wlComputeShape\":\"${var.JCSShape}\"}' > jcs.json"
  }
}
