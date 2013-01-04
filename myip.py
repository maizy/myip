# _*_ coding: utf-8 _*_
# Author: Nikita Kovaliov <nikita@maizy.ru>
# License: WTFPL


import webapp2


class MyIpHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        try:
            ip = self.request.remote_addr
        except:
            self.response.set_status(500)
            self.response.out.write('Houston, we have a problem')
            return
        self.response.out.write('{!s}\n'.format(ip))


app = webapp2.WSGIApplication([('/', MyIpHandler)])
