# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel
# Last Modification 09.2019
import os
import bpy

from io_mesh_w3d.export_utils_w3d import create_hierarchy, export_meshes, export_animation


def save(givenfilepath, _context, export_settings):
    """Start the w3d export and save to a .w3d file."""
    print('Saving file', givenfilepath)

    export_mode = export_settings['w3d_mode']
    print("export mode: " + str(export_mode))

    bpy.ops.object.mode_set(mode='OBJECT')

    containerName = (os.path.splitext(
        os.path.basename(givenfilepath))[0]).upper()

    (hierarchy, rig) = create_hierarchy(containerName)

    if export_mode in ('M', 'HAM'):
        sknFile = open(givenfilepath, "wb")
        export_meshes(sknFile, hierarchy, rig, containerName)

        if export_mode == 'HAM':
            hierarchy.header.num_pivots = len(hierarchy.pivots)
            hierarchy.write(sknFile)
        sknFile.close()
    elif export_mode == 'S':
        sklFile = open(givenfilepath, "wb")
        hierarchy.header.num_pivots = len(hierarchy.pivots)
        hierarchy.write(sklFile)
        sklFile.close()
    elif export_mode == 'A':
        aniFile = open(givenfilepath, "wb")
        export_animation(aniFile, containerName, hierarchy)
        aniFile.close()

    return {'FINISHED'}
