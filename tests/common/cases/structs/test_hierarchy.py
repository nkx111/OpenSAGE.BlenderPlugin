# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel

from tests.common.helpers.hierarchy import *
from tests.utils import TestCase


class TestHierarchy(TestCase):
    def test_write_read(self):
        expected = get_hierarchy()

        self.assertEqual(44, expected.header.size())
        self.assertEqual(636, expected.size(False))
        self.assertEqual(644, expected.size())

        self.write_read_test(expected, W3D_CHUNK_HIERARCHY, Hierarchy.read, compare_hierarchies, self, True)

    def test_write_read_minimal(self):
        expected = get_hierarchy_minimal()

        self.assertEqual(44, expected.header.size())
        self.assertEqual(132, expected.size(False))
        self.assertEqual(140, expected.size())

        self.write_read_test(expected, W3D_CHUNK_HIERARCHY, Hierarchy.read, compare_hierarchies, self, True)

    def test_write_read_empty(self):
        expected = get_hierarchy_empty()

        self.assertEqual(44, expected.header.size())
        self.assertEqual(44, expected.size(False))
        self.assertEqual(52, expected.size())

        self.write_read_test(expected, W3D_CHUNK_HIERARCHY, Hierarchy.read, compare_hierarchies, self, True)

    def test_validate(self):
        hierarchy = get_hierarchy()
        self.file_format = 'W3D'
        self.assertTrue(hierarchy.validate(self))
        self.file_format = 'W3X'
        self.assertTrue(hierarchy.validate(self))

        hierarchy.header.name = 'tooolonghieraname'
        self.file_format = 'W3D'
        self.assertFalse(hierarchy.validate(self))
        self.file_format = 'W3X'
        self.assertTrue(hierarchy.validate(self))

        hierarchy = get_hierarchy()
        hierarchy.pivots[1].name = 'tooolongpivotname'
        self.file_format = 'W3D'
        self.assertFalse(hierarchy.validate(self))
        self.file_format = 'W3X'
        self.assertTrue(hierarchy.validate(self))

    def test_unknown_chunk_skip(self):
        output = io.BytesIO()
        write_chunk_head(W3D_CHUNK_HIERARCHY, output, 9, has_sub_chunks=True)

        write_chunk_head(0x00, output, 1, has_sub_chunks=False)
        write_ubyte(0x00, output)

        io_stream = io.BytesIO(output.getvalue())
        (chunk_type, chunk_size, subchunk_end) = read_chunk_head(io_stream)

        self.assertEqual(W3D_CHUNK_HIERARCHY, chunk_type)

        self.warning = lambda text: self.assertEqual('unknown chunk_type in io_stream: 0x0', text)
        Hierarchy.read(self, io_stream, subchunk_end)

    def test_chunk_sizes(self):
        hierarchy = get_hierarchy_minimal()

        self.assertEqual(36, hierarchy.header.size(False))
        self.assertEqual(44, hierarchy.header.size())

        self.assertEqual(60, list_size(hierarchy.pivots, False))

        self.assertEqual(12, vec_list_size(hierarchy.pivot_fixups, False))

        self.assertEqual(132, hierarchy.size(False))
        self.assertEqual(140, hierarchy.size())

    def test_write_read_xml(self):
        self.write_read_xml_test(get_hierarchy(xml=True), 'W3DHierarchy', Hierarchy.parse, compare_hierarchies, self)

    def test_write_read_minimal_xml(self):
        self.write_read_xml_test(get_hierarchy_minimal(xml=True), 'W3DHierarchy', Hierarchy.parse, compare_hierarchies,
                                 self)
