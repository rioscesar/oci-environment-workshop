sudo bash -c "chmod 777 /tmp/StateInsurance.sql && mv /tmp/StateInsurance.sql /home/oracle/home"
sudo su - oracle -c "export ORACLE_SID=aTFdb && export ORAENV_ASK=NO && . /usr/local/bin/oraenv && exit | sqlplus / as sysdba @StateInsurance.sql"
