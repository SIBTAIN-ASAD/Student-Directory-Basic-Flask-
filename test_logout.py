import importlib
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch


class LogoutTests(unittest.TestCase):
    def setUp(self):
        # Isolate every test from the database, including app import-time setup.
        model_patch = patch('AddressBookModel.AddressBookModel')
        self.model_type = model_patch.start()
        self.addCleanup(model_patch.stop)
        self.module = importlib.import_module('app')
        self.model = self.model_type.return_value
        previous = self.module.model
        self.module.model = self.model
        self.addCleanup(setattr, self.module, 'model', previous)
        self.module.app.config['TESTING'] = True
        self.client = self.module.app.test_client()

    def test_logout_expires_both_cookies_and_blocks_followup_changes(self):
        self.client.set_cookie('user_id', '1')
        self.client.set_cookie('cid', '2')
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(self.client.get_cookie('user_id'))
        self.assertIsNone(self.client.get_cookie('cid'))
        for path in ('/create', '/delete', '/update', '/updateit'):
            with self.subTest(path=path):
                response = self.client.post(path)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Session ended', response.data)
        self.assertEqual(self.model.method_calls, [])

    def test_logout_without_cookies_is_idempotent(self):
        self.assertEqual(self.client.post('/logout').status_code, 200)
        self.assertEqual(self.client.post('/logout').status_code, 200)
        self.assertEqual(self.model.method_calls, [])

    def test_update_with_invalid_cookie_does_not_raise_server_error(self):
        self.client.set_cookie('user_id', 'invalid')
        self.client.set_cookie('cid', 'invalid')
        response = self.client.post('/updateit')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Session ended', response.data)
        self.assertEqual(self.model.method_calls, [])

    def test_logout_is_registered_before_server_start(self):
        def check_routes(app, **kwargs):
            self.assertIn('/logout', {rule.rule for rule in app.url_map.iter_rules()})
        with patch('flask.Flask.run', new=check_routes):
            runpy.run_path(str(Path(__file__).with_name('app.py')), run_name='__main__')


if __name__ == '__main__':
    unittest.main()
