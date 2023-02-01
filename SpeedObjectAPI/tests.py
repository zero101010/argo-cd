import pytest
import unittest

from main import app
class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        print(response.data)
    
    def test_velocity_with_params(self):
        tester = app.test_client(self)
        response = tester.get('/api/speed?distance=100&time=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,b'{"speed":"10.00m/s"}\n' )
    
    def test_velocity_without_params_time(self):
        tester = app.test_client(self)
        response = tester.get('/api/speed?distance=100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"error_message":"The parameter \'time\' is required"}\n')
        print(response.data)

    def test_velocity_without_params_distance(self):
        tester = app.test_client(self)
        response = tester.get('/api/speed?time=10')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data,b'{"error_message":"The parameter \'distance\' is required"}\n')
        print(response.data)

    def test_not_mapping_route(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data,b'{"error_message":"This page doesn\'t exist"}\n')

    
if __name__ == '__main__':
    unittest.main()