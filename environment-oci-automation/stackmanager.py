import argparse
import json
import os
import sys
import requests
import pprint
import time
# from account_info import AccountInfo

class StackManager():
    """ Class to do operations on Stackmanager """

    def __init__(self, username, password, domain_name, DEBUG):
        self.username = username
        self.password = password
        self.domain_name = domain_name
        self.DEBUG = DEBUG
        # account_info = AccountInfo(self.username, self.password, self.domain_name, self.DEBUG)
        # self.rest_url = account_info.get_jcs_rest_url()
        # print ("rest url is: --------------------------------------------------------------")
        # print (self.rest_url)
    
    def view_template(self):
        '''To view existing templates'''
        print ("I am here")

        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+ self.domain_name+"/templates/cst/instances"
        headers = {
            'X-ID-TENANT-NAME': '%s' %self.domain_name
            }
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint(headers)
            print("--------------------------------------------------------------------------")
        request = requests.get(url, headers=headers, auth=(self.username, self.password))

        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")

    def create_template(self, template_file):
        """To create template"""

        if self.DEBUG:
            print("**************************************************************************")
            print ("Inside create function for Template ")
            print("**************************************************************************")
        method = str('POST')
        files = {
            'template': (template_file, open(template_file, 'rb'))
            }
        ct = "multipart/form-data"
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+self.domain_name+"/templates/cst/instances"
        if self.DEBUG:
            print ("URL is : " + url)
            print("--------------------------------------------------------------------------")
            print ("File")
            print(files)
        header = {
            # "Content-Type" : "%s" % ct,
            "X-ID-TENANT-NAME" : "%s" % self.domain_name
        }
        
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint (header)
            print("--------------------------------------------------------------------------")
            
        request = requests.post(url, files = files, headers = header, auth=(self.username,self.password))
        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")
        
        time.sleep(30)

    def create_stack(self,stack_name, template_name):
        """To create SOA Stack"""

        if self.DEBUG:
            print("**************************************************************************")
            print ("Inside create function for JCS Stack ")
            print("**************************************************************************")
        method = str('POST')
        files = {
            'name' : "%s" %stack_name,
            'template': "%s" % template_name,
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"stackRegion.region\":\"us-ashburn-1\",\"stackRegion.availabilityDomain\":\"SyHU:US-ASHBURN-AD-2\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014412/TestDBBucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"_oF.f)I}0AEhfVxX.8.Q\",\"stackRegion.subnet\":\"Public Subnet SyHU:US-ASHBURN-AD-2\" }"
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"stackRegion.region\":\"us-ashburn-1\",\"stackRegion.availabilityDomain\":\"yKpP:US-ASHBURN-AD-2\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014412/JCS-Bucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"Dgw.EplvawC0_-NAJEa(\",\"stackRegion.subnet\":\"Public Subnet yKpP:US-ASHBURN-AD-2\" }"
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"PTvA:US-ASHBURN-AD-3\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00013851/myJCSbucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"A+&ks4jCb(p8v}7m}DkC\",\"subnet\":\"Public Subnet PTvA:US-ASHBURN-AD-3\" }"
            'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"Rewm:US-ASHBURN-AD-2\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014411/myJCSbucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"3Q#m>8y!HL61hv1Pd-NH\",\"subnet\":\"ocid1.subnet.oc1.iad.aaaaaaaaka62o2lrahypjca2bqwipjldonecsijezqlqduwpobah5isqrxha\",\"dbComputeShape\":\"VM.Standard1.1\", \"wlComputeShape\":\"VM.Standard1.1\"}"
            }
        ct = "multipart/form-data"
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+self.domain_name+"/services/stack/instances"
        if self.DEBUG:
            print ("URL is : " + url)
            print("--------------------------------------------------------------------------")
            print ("File")
            print(files)
        header = {
            # "Content-Type" : "%s" % ct,
            "X-ID-TENANT-NAME" : "%s" % self.domain_name
        }
        
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint (header)
            print("--------------------------------------------------------------------------")
            
        request = requests.post(url, files = files, headers = header, auth=(self.username,self.password))
        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")

    def create_soa_stack(self,stack_name, template_name):
        """To create SOA Stack"""
        #curl -i -X POST -u cloud.admin:hOMEly@7CAnAry \
        # -H "Content-Type:multipart/form-data" \
        # -H "X-ID-TENANT-NAME:idcs-2dcb6cc96da14fbe9e759ca6938c16e7" \
        # -F "name=myStack" \
        # -F "template=mytemplatemodified" \
        # -F 'parameterValues={"commonPwd":"Alpha2018_", "publicKeyText":"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA+yhdeLhdoZRtn7z2/2yjApulcmghQbure8n4rHCIOhWG+8yfVapEtwPkIDaxkVUimhU8hU32NdLPUBNpftNWsXrGL1yMug6NPgULoOd2lP+v+jtyJcUzk0hitAuG+wS62HEFmOvvZ8mGeYe20ZQ5ZrB1mUevrbNLYm7prb9ef/wCxONNGi+KjwlMOJpir2qEkM2cIcf+SP5aI2Q/IcV5wEGrudT06P2RxssJIp4ID7mTb+EcdI78NAOGb8rb0ak4zKLPfqrli9MuJYy9pSIxuc3ggNrdpAU/mAVS+1VL9N+86mOSUH5RkLRc847pFytZ3tpzlPOE/f0qhFISXHmleQ== rsa-key-20180313", "backupStorageContainer":{"cloudStorageContainer":"https://Storage-d71674de226942fb8afcead78d16bdc4.us.storage.oraclecloud.com/v1/Storage-d71674de226942fb8afcead78d16bdc4/StorageName","cloudStorageUser":"cloud.admin","cloudStoragePassword":"hOMEly@7CAnAry"}}' \
        # https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/idcs-2dcb6cc96da14fbe9e759ca6938c16e7/services/stack/instances
        if self.DEBUG:
            print("**************************************************************************")
            print ("Inside create function for SOA Stack ")
            print("**************************************************************************")
        files = {
            'name' : "%s" %stack_name,
            'template': "%s" % template_name,
            # 'parameterValue' : '{\\"publicKeyText\\":\\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp\\/pjNRyAGlR\\/\\/tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG\\/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1\\/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\\",\\"commonPwd\\":\\"Devops_123\\",\\"backupStorageContainer\\":{\\"cloudStorageContainer\\":\\"https:\\\\\\/\\/Storage-d71674de226942fb8afcead78d16bdc4.us.storage.oraclecloud.com\\\\\\/v1\\\\\\/Storage-d71674de226942fb8afcead78d16bdc4\\\\\\/StorageName\\",\\"cloudStorageUser\\":\\"cloud.admin\\",\\"cloudStoragePassword\\":\\"hOMEly@7CAnAry\\"}'
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\"},\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"Rewm:US-ASHBURN-AD-2\",\"backupStorageContainer\":{\"cloudStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014411/myJCSbucket\", \"cloudStorageUser\":\"gse-admin_ww@oracle.com\", \"cloudStoragePassword\": \"3Q#m>8y!HL61hv1Pd-NH\"},\"subnet\":\"ocid1.subnet.oc1.iad.aaaaaaaaka62o2lrahypjca2bqwipjldonecsijezqlqduwpobah5isqrxha\"}"
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\"},\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"Rewm:US-ASHBURN-AD-2\",\"subnet\":\"ocid1.subnet.oc1.iad.aaaaaaaaka62o2lrahypjca2bqwipjldonecsijezqlqduwpobah5isqrxha\"}"
            'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"Rewm:US-ASHBURN-AD-3\",\"backupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014411/myJCSbucket\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014411/myDBCSbucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"3Q#m>8y!HL61hv1Pd-NH\",\"subnet\":\"ocid1.subnet.oc1.iad.aaaaaaaavgbqkf5aiq6oodhfxv244aqkq6tpzt5ub4pu2bqmb6ru5bcylttq\",\"dbComputeShape\":\"VM.Standard1.1\", \"wlComputeShape\":\"VM.Standard1.2\", \"wlComputeShape2\":\"VM.Standard1.1\"}"
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"sRegion\":\"us-ashburn-1\",\"availabilityDomain\":\"uolW:US-ASHBURN-AD-3\",\"backupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014605/myJCSbucket\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00014605/myDBCSbucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"X8nTZ&M!&OK1MC3$zfwJ\",\"subnet\":\"ocid1.subnet.oc1.iad.aaaaaaaai2tqdaxmewxzsb26topp5pqcunoblxqijwv5k3g75pkien2jwd7q\",\"dbComputeShape\":\"VM.Standard1.1\", \"wlComputeShape\":\"VM.Standard1.2\", \"wlComputeShape2\":\"VM.Standard2.1\"}"
            # 'parameterValues' : "{\"publicKeyText\":\"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAguhaYjpszwr6VHzQiZzRx1YybExmpgWWmQaYRtmJ8bk7IGkmmBrlRqOkRY8T0LXyJ42+xZWn9R0hY656Xp/pjNRyAGlR//tTB0wBbP30ZrkdltWfo59AAWrxLjDpEs4AcgYG/7clcv6vLnlX5bF7NGQ3FK0zxpC+MFdjthnzztfdrFjxN4UsSvE1/MCZNWqn8jXyWMdxu0AzTaWKAH6jTFCmuiVUHtFp6W5l1ut7bfJvjPq73CNmrbJtcRHUy+Kwv2mHvghjcu9XMK2V+3u829fTRhG6dBQlH9d6soVHxpJ1fb06MwY8+JRLNUhSZyA4gaXKY3YSkZw5WIuluLbPsQ== rsa-key-20180221\",\"commonPwd\":\"Devops_123\",\"dbBackupStorageContainer\":\"https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/gse00013851/JCSBucket\", \"backupStorageUser\":\"gse-admin_ww@oracle.com\", \"backupStoragePassword\": \"A+&ks4jCb(p8v}7m}DkC\"}"
        }            
        # ct = "multipart/form-data"
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+self.domain_name+"/services/stack/instances"
        if self.DEBUG:
            print ("URL is : " + url)
            print("--------------------------------------------------------------------------")
            print ("File")
            print(files)
        header = {
            # "Content-Type" : "%s" % ct,
            "X-ID-TENANT-NAME" : "%s" % self.domain_name
        }
        
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint (header)
            print("--------------------------------------------------------------------------")
            print ("Sender Body : ")
            pprint.pprint (files)
            print("--------------------------------------------------------------------------")
            
        request = requests.post(url, files = files, headers = header, auth=(self.username,self.password))
        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")

    def view_stack(self):
        '''To view existing stacks'''
        print ("I am here inside view stack")
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+ self.domain_name+"/services/stack/instances"
        headers = {
            'X-ID-TENANT-NAME': '%s' %self.domain_name
            }
        request = requests.get(url, headers=headers, auth=(self.username, self.password))

        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")

    def start_stack(self, stack_name):
        ''' To Start Stack '''
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/"+ self.domain_name+"/services/stack/instances/" + stack_name + "/start"
        headers = {
            'X-ID-TENANT-NAME': '%s' %self.domain_name
            }
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint(headers)
            print("--------------------------------------------------------------------------")
            print ("URL is: ")
            print(url)
            print("--------------------------------------------------------------------------")

        request = requests.post(url, headers=headers, auth=(self.username, self.password))
        
        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")
        
        if request.status_code in (400, 409):
            json_response = json.loads(request.text)
            status = json_response["service_details"]["state"]
            while status=="INITIALIZING":
                time.sleep(30)
            if self.DEBUG:
                print (status)
        #curl -i -X POST -u cloud.admin:pLUCky@3FlOor -H "X-ID-TENANT-NAME:gse00013027" https://psm.us.oraclecloud.com/paas/api/v1.1/instancemgmt/gse00013027/services/stack/instances/DevOpsStack1/start

    def check_status(self, job_id):
        # curl -i -X GET -u cloud.admin:hOMEly@7CAnAry -H "X-ID-TENANT-NAME:idcs-2dcb6cc96da14fbe9e759ca6938c16e7" https://psm.us.oraclecloud.com/paas/api/v1.1/activitylog/idcs-2dcb6cc96da14fbe9e759ca6938c16e7/stack/job/23370043
        url = "https://psm.us.oraclecloud.com/paas/api/v1.1/activitylog/"+ self.domain_name+"/stack/job/"+job_id
        headers = {
            'X-ID-TENANT-NAME': '%s' %self.domain_name
            }
        if self.DEBUG:
            print ("Header : ")
            pprint.pprint(headers)
            print("--------------------------------------------------------------------------")
            print ("URL is: ")
            print(url)
            print("--------------------------------------------------------------------------")
        request = requests.get(url, headers=headers, auth=(self.username, self.password))
        
        if self.DEBUG:
            print ("Response Header : ")
            pprint.pprint (request.headers)            
            print("--------------------------------------------------------------------------")               
            print ("Response Body : ")
            pprint.pprint (request.text)
            print("--------------------------------------------------------------------------")
            print ("Status Code is : " + str(request.status_code))
            print("--------------------------------------------------------------------------")
        
        if request.status_code in (200, 202):
            json_response = json.loads(request.text)
            try:
                status = json_response["status"]
                if self.DEBUG:
                    print (status)
                return status
            except:
                print("JSON status not exists. Stack is not created.")

    def view_jcs(self):
        """To view JCS  instances"""
        url = "https://jaas.oraclecloud.com/paas/api/v1.1/instancemgmt/"+self.domain_name+"/services/jaas/instances/DevOpsStack1JCS"
        if self.DEBUG:
            print("**************************************************************************")
            print ("Validating JCS ")
            print("**************************************************************************")
            print ("URL is : " + url)
        header = {
            "X-ID-TENANT-NAME": "%s" % self.domain_name
        }
        
        request = requests.get(url, headers=header, auth=(self.username, self.password))
        if self.DEBUG:
            print("----------------------------------------------------")
            print ("Response Status is : " + str(request.status_code))
            print("----------------------------------------------------")
            print ("Response body is: ")
            # pprint.pprint(request.text)
            print("----------------------------------------------------")
            print ("Response header is: ")
            pprint.pprint(request.headers)
            print("----------------------------------------------------")
        if request.status_code in (200, 202):
            json_response = json.loads(request.text)
            try:
                weblogic_url = json_response["WLS_ROOT"]
                if self.DEBUG:
                    print ("weblogic_url")
                    print (weblogic_url)
                return weblogic_url
            except:
                print("JSON status not exists. Stack is not created.")

    def view_jcs_access_rules(self):
        url = "https://jaas.oraclecloud.com/paas/api/v1.1/instancemgmt/"+self.domain_name+"/services/jaas/instances/DevOpsStack1JCS/accessrules"
        if self.DEBUG:
            print("**************************************************************************")
            print ("Validating JCS ")
            print("**************************************************************************")
            print ("URL is : " + url)
        header = {
            "X-ID-TENANT-NAME": "%s" % self.domain_name
        }
        
        request = requests.get(url, headers=header, auth=(self.username, self.password))
        if self.DEBUG:
            print("----------------------------------------------------")
            print ("Response Status is : " + str(request.status_code))
            print("----------------------------------------------------")
            print ("Response body is: ")
            pprint.pprint(request.text)
            print("----------------------------------------------------")
            print ("Response header is: ")
            pprint.pprint(request.headers)
            print("----------------------------------------------------")
        # if request.status_code in (200, 202):
        #     json_response = json.loads(request.text)
        #     try:
        #         weblogic_url = json_response["WLS_ROOT"]
        #         if self.DEBUG:
        #             print ("weblogic_url")
        #             print (weblogic_url)
        #         return weblogic_url
        #     except:
        #         print("JSON status not exists. Stack is not created.")



def main(args):
    """Main function to call the stackmanager"""
    stackmanager = StackManager(args.username, args.password, args.dname, args.debug)

    if args.action == "view":
        if args.service == "jcs":    
            print ("Inside view jcs")
            # stackmanager.view_stack()
            # stackmanager.view_jcs()
            # stackmanager.view_jcs_access_rules()
        
        if args.service == "soa":
            print ("Inside view soa")
            # stackmanager.view_template()
            

    if args.action == "create":

        if args.service == "jcs":                
            stackmanager.create_template("Oracle-JCS-DBCS-Template.yaml")
            stackmanager.create_stack("MeghaStackTestScript5", "JCS-DBCS-Template-megha-script5")
            
        # stackmanager.create_soa_stack("DevOpsStack1", "JCS-DBCS-Template")

        if args.service == "soa":
            stackmanager.create_template("SOA-FROM-JCS-Final.yaml")
            stackmanager.create_soa_stack("SOAFROMJCSFinal7", "SOA-FROM-JCS-Final7")
            

    if args.action == "start":    
        stackmanager.start_stack("DevOpsStack1")
    
    if args.action == "status":    
        stackmanager.check_status(args.jid)
    
    # if args.action == "delete":  
    #     stackmanager.delete_jcs_template()

    # if args.action == "validate":  
    #     stackmanager.validate_jcs()

class ParseValues(object):
    """Class to parse the values from command line"""
 
    def __init__(self):
        # print ("Inside init of parse values")
        parser = argparse.ArgumentParser(
            description="Add users information to do CRUD operation on StackManager",
            usage='''python stackmanager.py <create, delete, view> <enter an option>
                <jcs, soa> <Enter an option>
                <-u, --username> <enter username>
                <-p, --password> <Enter Password>
                <-dn, --dname> <Enter Domain Name>''')
 
        acts = ['auth', 'create', 'delete', 'view', 'start', 'status']
        services = ['jcs', 'soa']
        parser.add_argument('action',
                            choices=acts,
                            help="Required Field")
        parser.add_argument('service',
                            choices=services,
                            help="Required Field")
        parser.add_argument("-u", "--username",
                           help="Enter the username",
                           default=None)
        parser.add_argument("-p", "--password",
                            help="Enter the password",
                            default=None)
        parser.add_argument("-dn", "--dname",
                            help="Enter the domain name",
                            default=None)
        parser.add_argument("-j", "--jid",
                            help="Enter the job ID",
                            default=None)
        parser.add_argument("--debug",
                            help="print debug messages to stderr",
                            action = 'store_true')
        args = parser.parse_args()
        main(args)
 
if __name__ == "__main__":
    ParseValues()