import unittest
from unittest.mock import patch, MagicMock
from src.decorators import log
import logging
from io import StringIO


class TestLogDecorator(unittest.TestCase):

    def test_log_to_console(self):
        """Тестирует логирование в консоль."""
        @log()
        def sample_function(a, b):
            return a + b

        log_stream = StringIO()
        handler = logging.StreamHandler(log_stream)
        logging.getLogger("sample_function").addHandler(handler)

        result = sample_function(2, 3)

        self.assertEqual(result, 5)
        handler.flush()
        log_content = log_stream.getvalue()
        self.assertIn("Calling sample_function with args", log_content)
        self.assertIn("sample_function returned 5", log_content)

    def test_log_to_file(self):
        """Тестирует логирование в файл."""
        log_file = 'test.log'

        @log(filename=log_file)
        def sample_function(a, b):
            return a * b

        sample_function(2, 4)

        with open(log_file, 'r') as file:
            logs = file.read()
            self.assertIn("Calling sample_function with args", logs)
            self.assertIn("sample_function returned 8", logs)

    def test_log_exception(self):
        """Тестирует логирование исключений."""
        @log()
        def sample_function(a, b):
            return a / b

        log_stream = StringIO()
        handler = logging.StreamHandler(log_stream)
        logging.getLogger("sample_function").addHandler(handler)

        with self.assertRaises(ZeroDivisionError):
            sample_function(1, 0)

        handler.flush()
        log_content = log_stream.getvalue()
        self.assertIn("raised ZeroDivisionError", log_content)


if __name__ == '__main__':
    unittest.main()
