import sys
sys.path.append("D:\python programms\strings")
import unittest
import nth_string_remove
class check(unittest.TestCase):
    def testcase(self):
        self.assertEqual(nth_string_remove.nth_string("prarthana",2),"prrthana")
if __name__=="__main__":
    unittest.main()
