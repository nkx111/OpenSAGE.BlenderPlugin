import bpy
from bpy.props import *
from bpy.types import Material

# property definition
# input name : custom property name
BuildingsSoviet={
    "PreviewHoles": "preview_holes",

    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "DamagedTexture":"damaged_texture",
    "EnvMult":"environment_mult",
}
BuildingsAllied = BuildingsSoviet
BuildingsJapan = BuildingsSoviet
BuildingsGenericDamageFill={
    "PreviewHoles": "preview_holes",

    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "DamagedTexture":"damaged_texture",
    "BumpScale":"bump_scale",
    "AmbientColor":"ambient_color",
    "DiffuseColor":"diffuse_color4",
    "SpecularColor":"specular_color",
    "SpecularExponent":"specular_intensity",
    "EnvMult":"environment_mult"
}

ObjectsSoviet={
    "DiffuseTexture":"diffuse_texture",
    "NormalMap":"normal_texture",
    "SpecMap":"spec_texture",
    "EnvMult":"environment_mult",
    "AlphaTestEnable":"alpha_test",
}
ObjectsAllied = ObjectsSoviet
ObjectsJapan = ObjectsSoviet
ObjectsAlliedTread = ObjectsSoviet

Infantry={
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
}

DefaultW3D={
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
    "TexCoordTransform_1":"tex_coord_transform_1"
}



material_parameter_map = {
    "BuildingsSoviet": BuildingsSoviet,
    "BuildingsAllied": BuildingsAllied,
    "BuildingsJapan": BuildingsJapan,
    "BuildingsGenericDamageFill": BuildingsGenericDamageFill,
    "ObjectsSoviet": ObjectsSoviet,
    "ObjectsAllied": ObjectsAllied,
    "ObjectsJapan": ObjectsJapan,
    "ObjectsAlliedTread": ObjectsAlliedTread,
    "Infantry": Infantry,
    "DefaultW3D": DefaultW3D,
}