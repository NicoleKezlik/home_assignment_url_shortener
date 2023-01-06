from django.test import TestCase,SimpleTestCase
from django.test import Client

# class Test(TestCase):
#     def test_1(self):
#         c = Client()
#         r = self.client.get('localhost:8000/2gSGGrX')
#         r.status_code
#         self.assertRedirect(response,'https://google.com',status_code=200,target_status_code=200,fetch_redirect_response=True)

class TestUrls(TestCase):
    short_url = ''

    def test_create(self):
        c = Client()
        r = c.post('/create/',{'url':'https://stackoverflow.com'})
        
        self.short_url = r.data[21:]
        print("111",self.short_url)
        assert(r.status_code==200)
        assert(r.data)

    def test_redirect(self):
        c = Client()
        r = c.get('google.com')
        print(r)
