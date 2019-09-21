from django.shortcuts import render, redirect
from testapp.models import Editor
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        self.var1 = data


def home_page(request):
    if request.method == 'POST':
        Editor.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Editor.objects.all().order_by('-dat').first()
    parser = MyHTMLParser()
    parser.feed(items.text)
    var1 = parser.var1
    return render(request, 'testapp/index.html', {'var1': var1})
