import unittest
import cli
import os
import subprocess


class TestCall(unittest.TestCase):
    def test_create_parser(self):
        parser = cli.create_parser()
        args = parser.parse_args(['config'])
        self.assertEqual(args.config, 'config')
        args = parser.parse_args(['go'])
        self.assertEqual(args.config, 'go')


    def test_create_conf_file(self):
        lines=["url=http://jenkins-url", "username=username:password", "jenkins_path=/home/user/projects/repo/Jenkinsfile"]
        with open(".test_env",'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
        f.close()
        self.assertTrue(os.path.isfile('.test_env'))


    def test_open_conf_file(self):
        self.assertEqual(cli.open_conf_file(),"Opening .env")

    def test_jenkins_client(self):
        assert(cli.jenkins_client(),"Jenkins-client not found\n jklint is going to download jenkins-cli.jar from your Jenkins server")
        pass


