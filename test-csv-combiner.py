import unittest
import io
import sys
import importlib
combiner = importlib.import_module("csv-combiner")

# methods names must start with "test_" or else test case won't run
class TestCombiner(unittest.TestCase):

    COL_VALUE = {
        "email_hash": "12345678",
        "category": "jacket"
    }

    def test_extract_columns_function_single_csv(self):
        file_names = ["accessories.csv"]
        self.assertEqual(combiner.extract_columns(file_names), ["email_hash", "category"])

    def test_extract_columns_function_multiple_csv(self):
        file_names = ["accessories.csv", "clothing.csv", "household_cleaners.csv"]
        self.assertEqual(combiner.extract_columns(file_names), ["email_hash", "category"])

    def test_extract_columns_function_different_columns(self):
        file_names = ["accessories.csv", "clothing.csv", "household_cleaners.csv", "shirts.csv"]
        self.assertEqual(combiner.extract_columns(file_names), ["email_hash", "category", "color"])

    def test_extract_columns_function_empty_list(self):
        file_names = []
        self.assertEqual(combiner.extract_columns(file_names), [])

    def test_create_row_valid(self):
        output_col_names = ["email_hash", "category"]
        self.assertEqual(combiner.create_row(self.COL_VALUE, output_col_names), "\"12345678\",\"jacket\"")

    def test_create_row_output_col_names_empty(self):
        output_col_names = []
        self.assertEqual(combiner.create_row(self.COL_VALUE, output_col_names), "")

    def test_create_row_output_col_val_empty(self):
        output_col_names = ["email_hash", "category"]
        self.assertEqual(combiner.create_row({}, output_col_names), "\"\",\"\"")

    def test_extract_rows_single_csv(self):
        output_column_names = ["email_hash", "color"]
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            with open("shirts.csv", 'r') as f:
                combiner.extract_rows(f, "shirts.csv", output_column_names)
            output = out.getvalue().strip()
            self.assertEqual(output, "\"s8e4f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6\",\"Black\"\n\"p5i3fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7\",\"Navy\"")
        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()

