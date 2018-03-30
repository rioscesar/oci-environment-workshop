resource "null_resource" "soa-manager" {
  provisioner "local-exec" {
    command = "echo '{\"publicKeyText\":\"${join(" ",slice(split(" ",file("${var.ssh_public_key_path}")),0,2))}\", \"commonPwd\":\"${var.db_password}\", \"sRegion\":\"${var.region}\", \"availabilityDomain\":\"${var.availability_domain}\", \"backupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"dbBackupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"backupStorageUser\":\"${var.object_storage_user}\", \"backupStoragePassword\": \"${var.swift_password}\", \"subnet\":\"${var.subnet}\", \"dbComputeShape\":\"${var.DBShape}\", \"wlComputeShape\":\"${var.SOAShape}\", \"wlComputeShape2\":\"${var.OTDShape}\"}' > soa.json"
  }
}


resource "null_resource" "jcs-manager" {
  provisioner "local-exec" {
    command = "echo '{\"publicKeyText\":\"${join(" ",slice(split(" ",file("${var.ssh_public_key_path}")),0,2))}\", \"commonPwd\":\"${var.db_password}\", \"sRegion\":\"${var.region}\", \"availabilityDomain\":\"${var.availability_domain}\", \"dbBackupStorageContainer\":\"https://swiftobjectstorage.${var.region}.oraclecloud.com/v1/${var.tenancy}/${var.bucket}\", \"backupStorageUser\":\"${var.object_storage_user}\", \"backupStoragePassword\": \"${var.swift_password}\", \"subnet\":\"${var.subnet}\", \"dbComputeShape\":\"${var.DBShape}\", \"wlComputeShape\":\"${var.JCSShape}\"}' > jcs.json"
  }
}

resource "null_resource" "stack-manager" {

  depends_on = ["null_resource.jcs-manager", "null_resource.soa-manager"]

  provisioner "local-exec" {
    command = "python stackmanager.py create jcs -u ${var.user} -p ${var.password} --debug -dn ${var.domain}"
  }

  provisioner "local-exec" {
    command = "python stackmanager.py create soa -u ${var.user} -p ${var.password} --debug -dn ${var.domain}"
  }
}
