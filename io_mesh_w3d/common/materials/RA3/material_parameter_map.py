import bpy
from bpy.props import *
from bpy.types import Material, PropertyGroup

# property definition
# input name : custom property name

material_parameter_map = {
("BuildingsSoviet", "BuildingsAllied", "BuildingsJapan", "BuildingsGeneric", "NormalMapped"): {
    "PreviewHoles": "preview_holes",

    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "DamagedTexture":"damaged_texture",
    "EnvMult":"environment_mult",
},

("BuildingsGenericDamageFill",) : {
    "PreviewHoles": "preview_holes",

    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "DamagedTexture":"damaged_texture",
    "BumpScale":"bump_uv_scale",
    "AmbientColor":"ambient_color",
    "DiffuseColor":"diffuse_color4",
    "SpecularColor":"specular_color",
    "SpecularExponent":"specular_intensity",
    "EnvMult":"environment_mult"
},

("ObjectsSoviet", "ObjectsAllied", "ObjectsJapan", "ObjectsGeneric", "ObjectsAlliedTread"):{
    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "EnvMult":"environment_mult",
    "AlphaTestEnable":"alpha_test",
},

("Infantry", "Tree", "BasicW3D"):{
    "ColorAmbient":"ambient_color",
    "ColorDiffuse":"diffuse_color3",
    "ColorSpecular":"specular_color",
    "Shininess":"specular_intensity",
    "ColorEmissive":"emission_color",
    "Texture_0":"texture_0",
    "DepthWriteEnable":"depth_write",
    "AlphaTestEnable":"alpha_test",
    "CullingEnable":"use_backface_culling",
    "BlendMode":"blend_mode",    
},

("DefaultW3D",):{
    "ColorAmbient":"ambient_color",
    "ColorDiffuse":"diffuse_color3",
    "ColorSpecular":"specular_color",
    "Shininess":"specular_intensity",
    "ColorEmissive":"emission_color",
    "EmissiveHDRMultipler":"emission_mult",
    "Opacity":"alpha",
    "EdgeFadeOut":"edge_fade_out",
    "NumTextures":"num_textures",
    "Texture_0":"texture_0",
    "Texture_1":"texture_1",
    "UseRecolorColors":"use_recolor",
    "HouseColorPulse":"house_color_pulse",
    "UseWorldCords":"use_world",
    "DepthWriteEnable":"depth_write",
    "AlphaTestEnable":"alpha_test",
    "CullingEnable":"use_backface_culling",
    "BlendMode":"blend_mode",
    "SecondaryTextureBlendMode":"secondary_texture_blend_mode",
    "TexCoordMapper_0":"tex_coord_mapper_0",
    "TexCoordTransform_0":"tex_coord_transform_0",
    "TextureAnimation_FPS_NumPerRow_LastFrame_FrameOffset_0":"tex_ani_fps_NPR_lastFrame_frameOffset_0",
    "TexCoordMapper_1":"tex_coord_mapper_1",
    "TexCoordTransform_1":"tex_coord_transform_1",

    "PreviewScrolling": "preview_scrolling"
},

("Simple",):{
    "ColorEmissive": "emission_color",
    "Texture_0":"texture_0",
    "TexCoordTransform_0": "tex_coord_transform_0",
    "DepthWriteEnable":"depth_write",
    "AlphaBlendingEnable": "alpha_blend",
    "FogEnable": "fog_enable"
},

("Simplest",):{
    "BaseTexture": "diffuse_texture"
},

# ("TreeSway"):{
#     "DiffuseTexture":"diffuse_texture",
#     "AmbientColor":"ambient_color",
#     "DiffuseColor":"diffuse_color4",
#     "AlphaTestEnable":"alpha_test",
#     "SwayEnable":"",
#     "Amp1":"",
#     "Freq1":"",
#     "Phase1":"",
# },

("FXLightning",):{
    "Texture_0":"texture_0",
    "ColorDiffuse":"diffuse_color3",
    "EmissiveHDRMultipler":"emission_mult",
    "MultiTextureEnable": "multi_texture_enable",
    "DiffuseCoordOffset": "diffuse_coord_offset",
    "MultiplyBlendEnable":"multiply_blend_enable",
    "EdgeFadeOut":"edge_fade_out",
    "Texture_1":"texture_1",
    "UniqueWorldCoordEnable":"unique_coord_enable",
    "UniqueWorldCoordScalar":"unique_coord_scalar",
    "UniqueWorldCoordStrength":"unique_coord_strength",
    "DisplaceScalar":"disp_scalar",
    "DisplaceAmp":"disp_amp",
    "DisplaceDivergenceAngle":"disp_angle",
    "DisplaceSpeed":"disp_speed",
    "UseRecolorColors":"use_recolor",
    "CullingEnable":"use_backface_culling",

}
}

def get_material_map(context, material_name):
    for keys in material_parameter_map:
        for key in keys:
            if str.upper(material_name) == str.upper(key):
                return key, material_parameter_map[keys]
    print(f'shader class not in defined: {material_name}. Use DefaultW3D!')
    return "DefaultW3D", material_parameter_map[("DefaultW3D",)]

material_type_items = []
for keys in material_parameter_map:
    for key in keys:
        material_type_items.append((key, key, ''))
material_type_items.append(('VERTEX_MATERIAL', 'VERTEX_MATERIAL', ''))
