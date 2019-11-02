# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel

import unittest
import io

from io_mesh_w3d.structs.struct import HEAD
from io_mesh_w3d.structs.w3d_texture import Texture, TextureInfo, W3D_CHUNK_TEXTURE
from io_mesh_w3d.io_binary import read_chunk_head
from tests.helpers.w3d_texture import *


class TestTexture(unittest.TestCase):
    def test_write_read(self):
        expected = get_texture()

        self.assertEqual(20, expected.texture_info.size())
        self.assertEqual(48, expected.size())

        io_stream = io.BytesIO()
        expected.write(io_stream)
        io_stream = io.BytesIO(io_stream.getvalue())

        (chunkType, chunkSize, chunkEnd) = read_chunk_head(io_stream)
        self.assertEqual(W3D_CHUNK_TEXTURE, chunkType)
        self.assertEqual(expected.size(False), chunkSize)

        actual = Texture.read(self, io_stream, chunkEnd)
        compare_textures(self, expected, actual)

    def test_minimal_write_read(self):
        expected = get_texture_empty()

        self.assertEqual(18, expected.size())

        io_stream = io.BytesIO()
        expected.write(io_stream)
        io_stream = io.BytesIO(io_stream.getvalue())

        (chunkType, chunkSize, chunkEnd) = read_chunk_head(io_stream)
        self.assertEqual(W3D_CHUNK_TEXTURE, chunkType)
        self.assertEqual(expected.size(False), chunkSize)

        actual = Texture.read(self, io_stream, chunkEnd)
        compare_textures(self, expected, actual)

    def test_chunk_sizes(self):
        tex = get_texture_minimal()

        self.assertEqual(12, tex.texture_info.size(False))
        self.assertEqual(12 + HEAD, tex.texture_info.size())

        self.assertEqual(30, tex.size(False))
        self.assertEqual(30 + HEAD, tex.size())
