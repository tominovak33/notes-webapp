import jinja2
import os
import site_details
import helpers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def render_page(template_name, variables, self):
    # join the 'global' template variables to the page specific ones that are explicitly supplied
    variables = helpers.merge_many(variables, site_details.global_details, {'site_url': self.request.host_url})

    template_file = "templates/" + template_name + ".html"
    template = JINJA_ENVIRONMENT.get_template(template_file)
    self.response.out.write(template.render(variables))
