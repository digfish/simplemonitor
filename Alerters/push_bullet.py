from pushbullet import Pushbullet
from alerter import Alerter

class PushBulletAlerter(Alerter):

    key = ""
    pb = None

    def __init__(self, config_options):
        Alerter.__init__(self, config_options)
        try:
            self.key = config_options["api_key"]
        except:
            raise RuntimeError("Required configuration fields missing")

        try:
            self.pb = Pushbullet(self.key)
        except Exception as ex:
            print ex
            raise RuntimeError("Something gone wrong when creating the PushBullet instance")


    def send_alert(self, name, monitor):

        type = self.should_alert(monitor)

        if type != "failure":
            return

        push = self.pb.push_note( name + " on " + monitor.running_on, monitor.get_result() )
