sudo bash -c "mv /tmp/StateInsurance.sql /home/oracle/home"
sudo su - oracle -c "export ORACLE_SID=aTFdb && export ORAENV_ASK=NO && . /usr/local/bin/oraenv && sqlplus / as sysdba @StateInsurance.sql"
