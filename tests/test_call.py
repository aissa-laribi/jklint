import unittest
import call
import unittest


class TestCall(unittest.TestCase):
    def test_lint(self):
        self.assertIn('jenkins-url',call.lint())
        self.assertIn('user',call.lint())
        self.assertIn('Jenkinsfile successfully validated.',call.lint())



