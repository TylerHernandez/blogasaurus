import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HtmlHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('TestHandler')
        template= jinja_env.get_template('solution/templates/fortune_welcome.html')
        testvariable= {
            "list_name" : ["1", "2", "3", "4", "5"],
        }
        self.response.write(template.render(testvariable))
app = webapp2.WSGIApplication([
        ('/', HtmlHandler)
], debug=True)
