![](images/200/Picture-lab.png)  
Updated: 04/02/2018

## Introduction

 This lab tutorial shows you how to deploy an Oracle Service Bus application to Oracle SOA Suite Cloud Service.

**_To log issues_**, click here to go to the [github oracle](https://github.com/oracle/learning-library/issues/new) repository issue submission form.

## Objectives

- Using this lab, you can deploy your Oracle Service Bus applications to Oracle SOA Suite Cloud Service. Because this cloud service uses the same Oracle SOA Suite software that you use for your on-premises applications, you can use the same tools in the cloud.

## Required Artifacts

- SOACS instance must be up and running before running the lab.

# Deploying an Oracle Service Bus Application to Oracle SOA Suite Cloud Service

## Service bus console application

### **STEP 1**: Login to your Oracle cloud account using **username** and **password**

- Login to your Oracle cloud account using **username** and **password** given by the instructor.

	![](images/200/1.png) 

- On the dashboard you can see a SOA instance running. Click on it.

	![](images/200/2.png) 	

- On the next page, click on "Open Service Console".
	
	![](images/200/3.png)

- Now, you can see a SOACS instance. From the "hamburger" menu on right, click on "Open Service Bus Console".

	![](images/200/4.png)	

- Login to service bus console using the **username** and **password**.

	![](images/200/5.png) 

- This will open the service bus console.

	![](images/200/6.png) 	

- Click on "Create" on the left hand side.
	
	![](images/200/7.png)

- Now, click on "import config jar" as shown below.

	![](images/200/8.png)

- It should open a new window to import the jar file. Click on Browse.

	![](images/200/9.png)

- Browse the zar file and open it.

	![](images/200/10.png)

- Click on next arrow mark.

	![](images/200/11.png)

- Accept the default values and Click on "Import".

	![](images/200/12.png)

- A success message would be popped if the import is successful. Hit Close.

	![](images/200/13.png)	

- On the left hand panel, you will see your project that was imported. Expand it by clicking on the expanstion button.
	
	![](images/200/14.png)

- Click on the business service for the project as shown below in the screenshot.

	![](images/200/15.png)

- This opens up the business process definition. On the left hand side click on "Transport".
	
	![](images/200/16.png)

- The endpoint URL's need to be modified so that it points the application being deployed on Cloud. If the endpoint is pointing to localhost replace with actual ip of the app on cloud.

	![](images/200/17.png) 

- The actual url should something like this.

	![](images/200/18.png) 

- Click on "Activate".

	![](images/200/19.png)

- Confirm the session activation. This should activate the service.

	![](images/200/20.png)
			
- You can test the service by clicking on green button for test console on the right hand side.

	![](images/200/21.png)

- This opens up a new window for testing. Choose the method you want to test. From the dropdown shown below choose the method to test.

	![](images/200/22.png)

- Click on "execute" to invoke the service and see test results.

	![](images/200/23.png)

- In the response document, you should be able to see the response returned by your service.

	![](images/200/24.png)

- This completes the manual SOA deployment section for this part of the Lab.



		

