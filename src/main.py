from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import pygeoip
import splittedDat

class MainPage(webapp.RequestHandler):
    
    def get(self):
        ip = self.request.remote_addr
        plik=splittedDat.splitedDat('dat/GeoLiteCity.dat')
        gic = pygeoip.GeoIP(filename='dat/GeoLiteCity.dat',filehandle=plik)
        region = gic.record_by_name(ip)
        
        self.response.headers['Content-Type'] = 'text/plain'
        if region is not None:
            for key in region:
                self.response.out.write('%s = %s\n' %(key,region[key]));
        else:
            self.response.out.write("Location not found\n");
        
application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
