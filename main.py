import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HtmlHandler(webapp2.RequestHandler):
    def get(self):
         #self.response.write('TestHandler')
        template= jinja_env.get_template('index.html')
        testvariable= {
            "list_name" : ["1", "2", "3", "4", "5"],
        }
        self.response.write(template.render(testvariable))

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())
class BlogHandler2(webapp2.RequestHandler):
    def post(self):
        variable= jinja_env.get_template('index.html')
        blogvar= {
        "title_var" : self.request.get('title'),
        "content_var" : self.request.get('content'),
        "author_var" : self.request.get('author'),
        }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(blogvar))

app = webapp2.WSGIApplication([
        ('/', HtmlHandler),
        ('/submit', BlogHandler),
        ('/submitted', BlogHandler2),
], debug=True)
