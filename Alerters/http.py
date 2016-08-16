'''
Created on Aug 15, 2016

@author: sam
'''

import urllib, urllib2

from alerter import Alerter


class HttpAlerter(Alerter):

    def __init__(self, config_options):
        Alerter.__init__(self, config_options)
        try:
            self.urlpath = config_options["urlpath"]
        except:
            raise RuntimeError("Required configuration fields missing")

    def send_alert(self, name, monitor):

        type = self.should_alert(monitor)

        if type != "failure":
            return

        params = {'title': 'alerter ' + name + " on " + monitor.running_on , \
                  'msg': monitor.get_result() }


        urlencoded = urllib.urlencode(params)

        final_url = self.urlpath + "?" + urlencoded
        print "Sending alert to ", final_url

        urllib2.urlopen( final_url ).read()


