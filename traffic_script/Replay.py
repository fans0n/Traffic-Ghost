from libmproxy.protocol.http import decoded                
import mitmproxy.http
from mitmproxy import ctx, http


class Replay:
    '''def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "" or not flow.request.path.startswith("/s"):
            return

        if "wd" not in flow.request.query.keys():
            ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
            return

        ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        flow.request.query.set_all("xxxx", ["xxxxx"])
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "xxxxxxxxx":
            return

        text = flow.response.get_text()
        text = text.replace("xxxx", "xxxx")
        flow.response.set_text(text)'''
        
    def response(context, flow):
        if flow.response.headers.get_first("content-type", "").startswith("image"):
        	with decoded(flow.response):
                try:
                	img = cStringIO.StringIO(open('xxx.jpg', 'rb').read())
                	flow.response.content = img.getvalue()
                	flow.response.headers["content-type"] = ["image/jpeg"]
                except:
                    pass



