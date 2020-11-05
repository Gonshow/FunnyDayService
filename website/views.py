from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "gonshow"
        ctxt["answers"] = [
            "母親に通知がいく",
            "ハグしてくる",
        ]
        return ctxt
