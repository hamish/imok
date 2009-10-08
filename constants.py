import os

class Constants():
    def domain(self):
        domain = os.environ['HTTP_HOST']
        if (not domain):
            domain = "i-am-ok.appspot.com"
        return domain
    def adminFrom(self):
        return "imok@currie.com.au"
    
        # create fake customer to be used on the settings page
    def fakeCustomer(self, account):
        return {'name': '<span name="nameSample"></span>',
                'timeSinceNotification': '<span name="timeoutSample"></span>',
                'phone': '<span name="phoneSample"></span>',
                'mobile': '<span name="mobileSample"></span>',
                'comment': '<textarea id="comment" name="comment" class="comment" rows="10" cols="10">%s</textarea>' % account.comment,
                }
    def fakeAlert(self, account):
        return {
                 'key': {'id':'fake'}, 
                 'check' : 'fake',
                }    