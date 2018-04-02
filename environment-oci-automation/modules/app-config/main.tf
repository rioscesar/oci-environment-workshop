resource "null_resource" "config-scripts" {
  provisioner "file" {
    connection {
      host = "${var.public-ip}" 
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }
    source      = "scripts/"
    destination = "/tmp/"
  }
}

resource "null_resource" "config-installer" {
 provisioner "file" {
   connection {
     host = "${var.public-ip}" 
     user = "${var.instance_user}"
     private_key = "${var.ssh_private_key}"
   }
   source      = "installer/"
   destination = "/tmp/"
 }
}

resource "null_resource" "weblogic-config" {

  depends_on = ["null_resource.config-installer", "null_resource.config-scripts"]
  
  provisioner "remote-exec" {
    connection {
      host= "${var.public-ip}"
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }
    
    inline = [
      "chmod +x /tmp/install_weblogic.sh",	
      "sudo /tmp/install_weblogic.sh"
    ]
  }
}

resource "null_resource" "insurance-scripts" {

  count = "${var.DeployInsuranceApp}"
  
  provisioner "file" {
    connection {
      host = "${var.public-ip}" 
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }
    source      = "apps/"
    destination = "/tmp/"
  }
}

resource "null_resource" "insurance-config" {

  count = "${var.DeployInsuranceApp}"

  depends_on = ["null_resource.weblogic-config", "null_resource.insurance-scripts"]
  
  provisioner "remote-exec" {
    connection {
      host= "${var.public-ip}"
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }

    inline = [
      "sleep 1m",
      "sudo docker cp /tmp/LibertyInsurance-WebServiceApp-context-root.war wlsadmin:/u01/oracle/",
      "sudo docker exec -it -u root wlsadmin wlst /u01/oracle/deploy_insurance_app.py"
    ]
  }
}

resource "null_resource" "state-scripts" {

  count = "${var.DeployStateApp}"
  
  provisioner "file" {
    connection {
      host = "${var.public-ip}" 
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }
    source      = "apps/"
    destination = "/tmp/"
  }
}

resource "null_resource" "state-config" {

  count = "${var.DeployStateApp}"

  depends_on = ["null_resource.weblogic-config", "null_resource.insurance-config", "null_resource.state-scripts"]
  
  provisioner "remote-exec" {
    connection {
      host= "${var.public-ip}"
      user = "${var.instance_user}"
      private_key = "${var.ssh_private_key}"
    }

    inline = [
      "sudo docker cp /tmp/StateGov-WebService-context-root.war wlsadmin:/u01/oracle/",
      "sudo docker exec -it -u root wlsadmin wlst /u01/oracle/deploy_state_app.py"
    ]
  }
}
