"""Basic test to verify package structure and imports."""
import unittest


class TestPackageStructure(unittest.TestCase):
    """Test basic package structure."""

    def test_import_package(self):
        """Test that the package can be imported."""
        import openflow_schema
        self.assertIsNotNone(openflow_schema)

    def test_version_exists(self):
        """Test that version attribute exists."""
        import openflow_schema
        self.assertTrue(hasattr(openflow_schema, '__version__'))
        self.assertEqual(openflow_schema.__version__, '0.1.0')


if __name__ == '__main__':
    unittest.main()
