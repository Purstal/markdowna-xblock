"""TO-DO: Write a description of what this XBlock is."""


import json
import cgi

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblock.runtime import IdGenerator


class MarkdownXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    display_name = String(
        display_name=u"Display Name",
        default="Markdown",
        scope=Scope.settings
    )

    default_markdown_text = pkg_resources.resource_string(
        __name__, "static/res/default-markdown-text.txt").decode("utf8")

    markdown_text = String(
        default=unicode(default_markdown_text), scope=Scope.content,
        help="The markdown text you saved"
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the MarkdownXBlock, shown to students
        when viewing courses.
        """

        data = {}
        data['markdown_text'] = unicode(self.markdown_text)

        html = self.resource_string("static/html/markdowna_studentview.html")
        frag = Fragment(unicode(html.format(
            data=unicode(cgi.escape(json.dumps(data))))))

        # markdown it
        frag.add_javascript(self.resource_string(
            "static/js/lib/markdown-it_new.min.js"))

        # github markdown css
        frag.add_css(self.resource_string(
            "static/css/lib/github-markdown_new.css"))

        frag.add_javascript(self.resource_string(
            "static/js/src/markdowna_studentview.js"))

        frag.initialize_js('MarkdownXBlock')
        return frag

    def studio_view(self, context=None):
        data = {}
        data['markdown_text'] = unicode(self.markdown_text)

        html = self.resource_string("static/html/markdowna_studioview.html")
        frag = Fragment(unicode(html.format(
            data=unicode(cgi.escape(json.dumps(data))))))

        # markdown it
        frag.add_javascript(self.resource_string(
            "static/js/lib/markdown-it_new.min.js"))

        # simplemde
        frag.add_javascript(self.resource_string(
            "static/js/lib/simplemde_new.min.js"))
        frag.add_css(self.resource_string(
            "static/css/lib/simplemde.min.css"))

        # github markdown css
        frag.add_css(self.resource_string(
            "static/css/lib/github-markdown_new.css"))

        frag.add_javascript(self.resource_string(
            "static/js/src/markdowna_studioview.js"))

        frag.initialize_js('MarkdownXBlock')
        return frag

    @XBlock.json_handler
    def save_markdown_text(self, data, suffix=''):
        """
        a handler to update data
        """

        ret = {}

        if "markdown_text" in data:
            self.markdown_text = unicode(data["markdown_text"])
            ret["success"] = True
        else:
            ret["success"] = False

        return ret  # {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Markdown",
             """<markdowna />
             """)
        ]
