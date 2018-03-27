resource "null_resource" "stack-manager" {
  provisioner "local-exec" {
    command = "python stackmanager.py create soa -u cloud.admin -p StariNg@9Scent --debug -dn idcs-72b2b9f4472e4a80ab7e5e0c1e629688"
    command = "python stackmanager.py create jcs -u cloud.admin -p StariNg@9Scent --debug -dn idcs-72b2b9f4472e4a80ab7e5e0c1e629688"
  }
}
