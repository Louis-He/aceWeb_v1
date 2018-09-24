import web

urls = (
    '', 'index',
    '/index', 'index',
)

class index:
    def GET(self):
        result = open(r'index.html', 'r').read()
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
