import re
import sys
 
warPath = '/u01/oracle/StateGov-WebService-context-root.war'
appName = 'StateApp'

weblogicUrl = sys.argv[1]+':7001'
userName = 'weblogic'
password = 'DevOps_123#'

connect(userName, password, weblogicUrl)
 
appList = re.findall(appName, ls('/AppDeployments'))
if len(appList) >= 1:
    print 'undeploying application'
    undeploy(appName)
 
deploy(appName, path = warPath, retireTimeout = -1, upload = 'True')
exit()

