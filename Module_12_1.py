import Test_git
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Test_git.Runner("Runner_1")
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Test_git.Runner('Runner_2')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Test_git.Runner('Runner_3')
        runner_4 = Test_git.Runner('Runner_4')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance, 'different results')


if __name__ == '__main__':
    unittest.main()