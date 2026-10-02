import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ("week1.ipynb", "week2.ipynb")


class NotebookSyntaxTests(unittest.TestCase):
    def test_notebooks_are_valid_json_and_code_cells_compile(self):
        for notebook_name in NOTEBOOKS:
            with self.subTest(notebook=notebook_name):
                notebook_path = REPO_ROOT / notebook_name
                notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
                self.assertEqual(notebook.get("nbformat"), 4)
                for cell_number, cell in enumerate(notebook.get("cells", [])):
                    if cell.get("cell_type") == "code":
                        with self.subTest(notebook=notebook_name, cell=cell_number):
                            compile(cell.get("source", ""), f"{notebook_name}:cell-{cell_number}", "exec")

    def test_notebooks_offer_configurable_and_local_data_paths(self):
        for notebook_name in NOTEBOOKS:
            with self.subTest(notebook=notebook_name):
                notebook = json.loads((REPO_ROOT / notebook_name).read_text(encoding="utf-8"))
                source = "\n".join(
                    cell.get("source", "")
                    for cell in notebook.get("cells", [])
                    if cell.get("cell_type") == "code"
                )
                self.assertIn("TITANIC_TRAIN_CSV", source)
                self.assertIn("data/train.csv", source)
                self.assertIn("/kaggle/input/competitions/titanic/train.csv", source)


if __name__ == "__main__":
    unittest.main()
