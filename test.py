import unittest
import os
from time import strftime, gmtime

import database
import sys
import datetime

class TestDatabase(unittest.TestCase):
    filename = "" #linux

    currentResult = None

    def setUp(self) -> None:
        os.chdir("/tmp")
        self.filename = "hello.db"

    def tearDown(self):
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        log_file = open("/tmp/log-phonebook.txt", 'w')
        if not ok:
            os.putenv("LAST_PHONE_LOG_RESULT", "1")
            typ, text = ('ERROR', error) if error else ('FAIL', failure)
            msg = [x for x in text.split('\n')[1:] if not x.startswith(' ')][0]
            log_file.write("\n%s: %s\n     %s" % (typ, self.id(), msg))
        else:
            os.putenv("LAST_PHONE_LOG_RESULT", "0")
        log_file.close()


    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def run(self, result=None):
        self.currentResult = result
        unittest.TestCase.run(self, result)

    def test_init(self):
        file = open(self.filename, 'w+').close()
        self.assertEqual(database.init_db(self.filename), 0, "norm file")
        fake_filename = "C:\\[p[fake_filename"
        self.assertEqual(database.init_db(fake_filename), 1, "fake file db")

    def test_add(self):
        file = open(self.filename, 'w+').close()
        database.init_db(self.filename)
        args = {"f":"fe", "fa":"fe", "fb":"fe", "cf":"fe"}
        self.assertEqual(0, database.append_db(args), "4 args for append")
        args = {"f": "fe", "fa": "fe", "fb": "fe", "cf": "fe", "jkl":"jr"}
        self.assertEqual(1, database.append_db(args), "more than 4 args")

    def test_search(self):
        file = open(self.filename, 'w+').close()
        database.init_db(self.filename)
        args = {"name":"k","surname":"k","phone":"l","birthday":"k"}
        database.append_db(args)
        result = database.search_db(args)
        self.assertEqual([('k', 'k', 'l', 'k')], result, "right search")




if __name__ == '__main__':
    unittest.main()