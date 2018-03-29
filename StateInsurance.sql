alter session set "_ORACLE_SCRIPT"=true; 

CREATE USER stateinsurance IDENTIFIED BY "STateinsurance12@_"
DEFAULT TABLESPACE users
TEMPORARY TABLESPACE temp
QUOTA UNLIMITED ON users;

GRANT CONNECT, DBA to stateinsurance;

GRANT create table, create sequence to stateinsurance;

GRANT all privileges to stateinsurance;

--------------------------------------------------------
--  DDL for Table CUSTOMER
--------------------------------------------------------

  CREATE TABLE "STATEINSURANCE"."CUSTOMER" 
   (	"INC_ID" VARCHAR2(20 BYTE), 
	"NAME" VARCHAR2(20 BYTE), 
	"ADDRESS" VARCHAR2(20 BYTE), 
	"PHONE" VARCHAR2(20 BYTE), 
	"SSN" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into STATEINSURANCE.CUSTOMER
SET DEFINE OFF;
Insert into STATEINSURANCE.CUSTOMER (INC_ID,NAME,ADDRESS,PHONE,SSN) values ('1','cesar','7920','9999','ssss');
Insert into STATEINSURANCE.CUSTOMER (INC_ID,NAME,ADDRESS,PHONE,SSN) values ('2','Eastern','EIP Main','string','Stuff');
--------------------------------------------------------
--  DDL for Index CUSTOMER_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "STATEINSURANCE"."CUSTOMER_PK" ON "STATEINSURANCE"."CUSTOMER" ("INC_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Trigger CUSTOMER_TRG
--------------------------------------------------------

  CREATE OR REPLACE NONEDITIONABLE TRIGGER "STATEINSURANCE"."CUSTOMER_TRG" 
BEFORE INSERT ON CUSTOMER 
FOR EACH ROW 
BEGIN
  <<COLUMN_SEQUENCES>>
  BEGIN
    IF INSERTING AND :NEW.INC_ID IS NULL THEN
      SELECT CUSTOMER_SEQ1.NEXTVAL INTO :NEW.INC_ID FROM SYS.DUAL;
    END IF;
  END COLUMN_SEQUENCES;
END;
/
ALTER TRIGGER "STATEINSURANCE"."CUSTOMER_TRG" ENABLE;
--------------------------------------------------------
--  Constraints for Table CUSTOMER
--------------------------------------------------------

  ALTER TABLE "STATEINSURANCE"."CUSTOMER" MODIFY ("INC_ID" NOT NULL ENABLE);
  ALTER TABLE "STATEINSURANCE"."CUSTOMER" MODIFY ("NAME" NOT NULL ENABLE);
  ALTER TABLE "STATEINSURANCE"."CUSTOMER" ADD CONSTRAINT "CUSTOMER_PK" PRIMARY KEY ("INC_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
