'''
AWS ELB needs Content-Length set (and non-zero) on responses to consider an EC2 instance healthy
'''
class ContentLengthMiddleware():
    def process_response(self, request, response):
        response['Content-Length'] = len(response.content)
        return response