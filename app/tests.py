from django.test import TestCase,SimpleTestCase
from django.test import Client
from app.models import Urls

# class Test(TestCase):
#     def test_1(self):
#         c = Client()
#         r = self.client.get('localhost:8000/2gSGGrX')
#         r.status_code
#         self.assertRedirect(response,'https://google.com',status_code=200,target_status_code=200,fetch_redirect_response=True)

class TestUrls(TestCase):

    def test_create(self):
        # create new url, using post api
        c = Client()
        r = c.post('/create/',{'url':'https://stackoverflow.com'})
        assert(r.status_code==200)

    def test_redirect(self):
        # create a test url object
        short_url = 'abc'
        original_url = "https://stackoverflow.com"
        Urls(origin_url = original_url,short_url = short_url).save()
        # check that the short url redirects to the original url
        c = Client()
        r = c.get('/'+short_url)
        assert(r.status_code==302)
        assert(r.url == original_url)

    def test_incorrect_short_url(self):
        # check in correct url and make sure it does not exist
        c = Client()
        r = c.get('/aaa')
        assert(r.status_code==404)
