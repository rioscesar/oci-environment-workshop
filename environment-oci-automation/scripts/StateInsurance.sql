alter session set "_ORACLE_SCRIPT"=true; 

CREATE USER stateinsurance IDENTIFIED BY "DevOps_123#"
DEFAULT TABLESPACE users
TEMPORARY TABLESPACE temp
QUOTA UNLIMITED ON users;

GRANT CONNECT, DBA to stateinsurance;

GRANT create table, create sequence to stateinsurance;

GRANT all privileges to stateinsurance;

--------------------------------------------------------
--  DDL for Table INSURANCE
--------------------------------------------------------

  CREATE TABLE "STATEINSURANCE"."INSURANCE" 
   (	"NAME" VARCHAR2(30 BYTE), 
	"ADDRESS" VARCHAR2(30 BYTE), 
	"PHONE" VARCHAR2(30 BYTE), 
	"SSN" VARCHAR2(30 BYTE), 
	"POLICY" VARCHAR2(30 BYTE), 
	"COMPANY" VARCHAR2(30 BYTE), 
	"EXP" DATE
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table STATE
--------------------------------------------------------

  CREATE TABLE "STATEINSURANCE"."STATE" 
   (	"NAME" VARCHAR2(30 BYTE), 
	"ADDRESS" VARCHAR2(30 BYTE), 
	"PHONE" VARCHAR2(30 BYTE), 
	"SSN" VARCHAR2(30 BYTE)
   ) SEGMENT CREATION DEFERRED 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
REM INSERTING into STATEINSURANCE.INSURANCE
SET DEFINE OFF;
REM INSERTING into STATEINSURANCE.STATE
SET DEFINE OFF;
--------------------------------------------------------
--  Constraints for Table INSURANCE
--------------------------------------------------------

  ALTER TABLE "STATEINSURANCE"."INSURANCE" MODIFY ("NAME" NOT NULL ENABLE);

