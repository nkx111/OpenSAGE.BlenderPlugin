import bpy
from bpy.props import *
from bpy.types import Material, PropertyGroup
from bpy_extras import node_shader_utils
from io_mesh_w3d.common.utils.helpers import *

Material.material_type = EnumProperty(
    name='Material Type',
    description='defines the type of the material',
    items=[
        ('BuildingsSoviet', 'BuildingsSoviet', 'desc: todo'),
        ('BuildingsAllied', 'BuildingsAllied', 'desc: todo'),
        ('BuildingsJapan', 'BuildingsJapan', 'desc: todo'),
        ('BuildingsGenericDamageFill', 'BuildingsGenericDamageFill', 'desc: todo'),

        ('ObjectsSoviet', 'ObjectsSoviet', 'desc: todo'),
        ('ObjectsAllied', 'ObjectsAllied', 'desc: todo'),
        ('ObjectsJapan', 'ObjectsJapan', 'desc: todo'),
        ('ObjectsAlliedTread', 'ObjectsAlliedTread', 'desc: todo'),

        ('Infantry', 'Infantry', 'desc: todo'),
        ('DefaultW3D', 'DefaultW3D', 'desc: todo'),

        ('VERTEX_MATERIAL', 'Vertex', 'desc: todo'),],
    default='VERTEX_MATERIAL')

Material.prelit_type = EnumProperty(
    name='Prelit Type',
    description='defines the prelit type of the vertex material',
    items=[
        ('PRELIT_UNLIT', 'Prelit Unlit', 'desc: todo'),
        ('PRELIT_VERTEX', 'Prelit Vertex', 'desc: todo'),
        ('PRELIT_LIGHTMAP_MULTI_PASS', 'Prelit Lightmap multi Pass', 'desc: todo'),
        ('PRELIT_LIGHTMAP_MULTI_TEXTURE', 'Prelit Lightmap multi Texture', 'desc: todo')],
    default='PRELIT_UNLIT')

Material.attributes = EnumProperty(
    name='attributes',
    description='Attributes that define the behaviour of this material',
    items=[
        ('DEFAULT', 'Default', 'desc: todo', 0),
        ('USE_DEPTH_CUE', 'UseDepthCue', 'desc: todo', 1),
        ('ARGB_EMISSIVE_ONLY', 'ArgbEmissiveOnly', 'desc: todo', 2),
        ('COPY_SPECULAR_TO_DIFFUSE', 'CopySpecularToDiffuse', 'desc: todo', 4),
        ('DEPTH_CUE_TO_ALPHA', 'DepthCueToAlpha', 'desc: todo', 8)],
    default=set(),
    options={'ENUM_FLAG'})

Material.surface_type = EnumProperty(
    name='Surface type',
    description='Describes the surface type for this material',
    items=[
        ('0', 'LightMetal', 'desc: todo'),
        ('1', 'HeavyMetal', 'desc: todo'),
        ('2', 'Water', 'desc: todo'),
        ('3', 'Sand', 'desc: todo'),
        ('4', 'Dirt', 'desc: todo'),
        ('5', 'Mud', 'desc: todo'),
        ('6', 'Grass', 'desc: todo'),
        ('7', 'Wood', 'desc: todo'),
        ('8', 'Concrete', 'desc: todo'),
        ('9', 'Flesh', 'desc: todo'),
        ('10', 'Rock', 'desc: todo'),
        ('11', 'Snow', 'desc: todo'),
        ('12', 'Ice', 'desc: todo'),
        ('13', 'Default', 'desc: todo'),
        ('14', 'Glass', 'desc: todo'),
        ('15', 'Cloth', 'desc: todo'),
        ('16', 'TiberiumField', 'desc: todo'),
        ('17', 'FoliagePermeable', 'desc: todo'),
        ('18', 'GlassPermeable', 'desc: todo'),
        ('19', 'IcePermeable', 'desc: todo'),
        ('20', 'ClothPermeable', 'desc: todo'),
        ('21', 'Electrical', 'desc: todo'),
        ('22', 'Flammable', 'desc: todo'),
        ('23', 'Steam', 'desc: todo'),
        ('24', 'ElectricalPermeable', 'desc: todo'),
        ('25', 'FlammablePermeable', 'desc: todo'),
        ('26', 'SteamPermeable', 'desc: todo'),
        ('27', 'WaterPermeable', 'desc: todo'),
        ('28', 'TiberiumWater', 'desc: todo'),
        ('29', 'TiberiumWaterPermeable', 'desc: todo'),
        ('30', 'UnderwaterDirt', 'desc: todo'),
        ('31', 'UnderwaterTiberiumDirt', 'desc: todo')],
    default='13')


Material.translucency = FloatProperty(
    name='Translucency',
    default=0.0,
    min=0.0, max=1.0,
    description='Translucency property')

Material.stage0_mapping = EnumProperty(
    name='Stage 0 Mapping',
    description='defines the stage mapping type of this material',
    items=[
        ('0x00000000', 'UV', 'desc: todo'),
        ('0x00010000', 'Environment', 'desc: todo'),
        ('0x00020000', 'Cheap Environment', 'desc: todo'),
        ('0x00030000', 'Screen', 'desc: todo'),
        ('0x00040000', 'Linear Offset', 'desc: todo'),
        ('0x00050000', 'Silhouette', 'desc: todo'),
        ('0x00060000', 'Scale', 'desc: todo'),
        ('0x00070000', 'Grid', 'desc: todo'),
        ('0x00080000', 'Rotate', 'desc: todo'),
        ('0x00090000', 'Sine Linear Offset', 'desc: todo'),
        ('0x000A0000', 'Step Linear Offset', 'desc: todo'),
        ('0x000B0000', 'Zigzag Linear Offset', 'desc: todo'),
        ('0x000C0000', 'WS Classic Environment', 'desc: todo'),
        ('0x000D0000', 'WS Environment', 'desc: todo'),
        ('0x000E0000', 'Grid Classic Environment', 'desc: todo'),
        ('0x000F0000', 'Grid Environment', 'desc: todo'),
        ('0x00100000', 'Random', 'desc: todo'),
        ('0x00110000', 'Edge', 'desc: todo'),
        ('0x00120000', 'Bump Environment', 'desc: todo')],
    default='0x00000000')

Material.stage1_mapping = EnumProperty(
    name='Stage 1 Mapping',
    description='defines the stage mapping type of this material',
    items=[
        ('0x00000000', 'UV', 'desc: todo'),
        ('0x00000100', 'Environment', 'desc: todo'),
        ('0x00000200', 'Cheap Environment', 'desc: todo'),
        ('0x00000300', 'Screen', 'desc: todo'),
        ('0x00000400', 'Linear Offset', 'desc: todo'),
        ('0x00000500', 'Silhouette', 'desc: todo'),
        ('0x00000600', 'Scale', 'desc: todo'),
        ('0x00000700', 'Grid', 'desc: todo'),
        ('0x00000800', 'Rotate', 'desc: todo'),
        ('0x00000900', 'Sine Linear Offset', 'desc: todo'),
        ('0x00000A00', 'Step Linear Offset', 'desc: todo'),
        ('0x00000B00', 'Zigzag Linear Offset', 'desc: todo'),
        ('0x00000C00', 'WS Classic Environment', 'desc: todo'),
        ('0x00000D00', 'WS Environment', 'desc: todo'),
        ('0x00000E00', 'Grid Classic Environment', 'desc: todo'),
        ('0x00000F00', 'Grid Environment', 'desc: todo'),
        ('0x00001000', 'Random', 'desc: todo'),
        ('0x00001100', 'Edge', 'desc: todo'),
        ('0x00001200', 'Bump Environment', 'desc: todo')],
    default='0x00000000')

Material.vm_args_0 = StringProperty(
    name='vm_args_0',
    description='Vertex Material Arguments 0',
    default='')

Material.vm_args_1 = StringProperty(
    name='vm_args_1',
    description='Vertex Material Arguments 1',
    default='')

Material.technique = IntProperty(
    name='Technique',
    description='Dont know yet',
    default=0,
    min=0,
    max=1)












Material.ambient_color = FloatVectorProperty(
    name='Ambient Color',
    subtype='COLOR',
    size=3,
    default=(1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Ambient color')

Material.diffuse_color4 = FloatVectorProperty(
    name='Diffuse4',
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Diffuse color with alpha')

Material.diffuse_color3 = FloatVectorProperty(
    name='Diffuse3',
    subtype='COLOR',
    size=3,
    default=(1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Diffuse color')

def OnEmissionMultChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    principled.emission_strength = self.emission_mult
Material.emission_mult = FloatProperty(
    name='Emissive HDR Multipler',
    default=1.0,
    min=0.0, max=1000.0,
    description='Additional Multiplier for the final color',
    update=OnEmissionMultChanged)

def OnTexture01Changed(self:Material, context):
    if self.blend_mode == 0:
        self.blend_method = "OPAQUE"
    else:
        if self.alpha_test == False:
            self.blend_method = "HASHED"    
        else:
            self.blend_method = "CLIP"  

    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    if (self.num_textures == 1 or self.texture_1 == "") and self.texture_0 != "":
        tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0)
        math_node_alpha = create_node_no_repeative(self, "ShaderNodeMath", "math_node_alpha")
        math_node_alpha.use_clamp = True
        math_node_alpha.operation = 'MULTIPLY' 
        math_node_alpha.inputs[1].default_value = self.alpha
        self.node_tree.links.new(tex_node.outputs["Color"], math_node_alpha.inputs[0])
        self.node_tree.links.new(math_node_alpha.outputs["Value"], principled.node_principled_bsdf.inputs["Alpha"])
        self.node_tree.links.new(tex_node.outputs["Color"], principled.node_principled_bsdf.inputs["Base Color"])

        # Add a node to combine two colors using multiply
        color_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "color_mix_node")
        color_mix_node.blend_type = 'MULTIPLY'
        color_mix_node.inputs[0].default_value = 0  # Mix factor
        color_mix_node.inputs[1].default_value = (*self.emission_color, 1.0)  # Convert to 4D vector
        self.node_tree.links.new(tex_node.outputs["Color"], color_mix_node.inputs[2])
        self.node_tree.links.new(color_mix_node.outputs["Color"], principled.node_principled_bsdf.inputs["Emission"])

    elif self.texture_0 != "" and self.texture_1 != "" and self.num_textures == 2:
        tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0)
        tex_node1 = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_1)

        uv_tex_0 = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_0")
        uv_tex_0.uv_map = "UVMap.001"
        uv_tex_1 = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_1")
        uv_tex_1.uv_map = "UVMap"

        self.node_tree.links.new(uv_tex_0.outputs['UV'], tex_node.inputs['Vector'])
        self.node_tree.links.new(uv_tex_1.outputs['UV'], tex_node1.inputs['Vector'])

        texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
        texture_mix_node.blend_type = 'MULTIPLY'
        texture_mix_node.inputs[0].default_value = 0  # Mix factor
        self.node_tree.links.new(tex_node.outputs["Color"], texture_mix_node.inputs[1])
        self.node_tree.links.new(tex_node1.outputs["Color"], texture_mix_node.inputs[2])

        math_node_alpha = create_node_no_repeative(self, "ShaderNodeMath", "math_node_alpha")
        math_node_alpha.use_clamp = True
        math_node_alpha.operation = 'MULTIPLY' 
        math_node_alpha.inputs[1].default_value = self.alpha
        self.node_tree.links.new(texture_mix_node.outputs["Color"], math_node_alpha.inputs[0])
        self.node_tree.links.new(math_node_alpha.outputs["Value"], principled.node_principled_bsdf.inputs["Alpha"])
        self.node_tree.links.new(tex_node.outputs["Color"], principled.node_principled_bsdf.inputs["Base Color"])

        # Add a node to combine two colors using multiply
        color_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "color_mix_node")
        color_mix_node.blend_type = 'MULTIPLY'
        color_mix_node.inputs[0].default_value = 0  # Mix factor
        color_mix_node.inputs[1].default_value = (*self.emission_color, 1.0)  # Convert to 4D vector
        self.node_tree.links.new(texture_mix_node.outputs["Color"], color_mix_node.inputs[2])
        self.node_tree.links.new(color_mix_node.outputs["Color"], principled.node_principled_bsdf.inputs["Emission"])

Material.emission_color = FloatVectorProperty(
    name='Emission Color',
    subtype='COLOR',
    size=3,
    default=(1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Emission color',
    update=OnTexture01Changed)

Material.alpha_test = BoolProperty(
    name='Alpha Test',
    description='Enable the alpha test. Pixels with alpha < 64/255 will be cliped. ',
    default=True,
    update=OnTexture01Changed)

Material.alpha = FloatProperty(
    name='Alpha Multiplier',
    default=1.0,
    min=0.0, max=10.0,
    description='Additional Multiplier for the alpha value',
    update=OnTexture01Changed)

Material.blend_mode = IntProperty(
    name='Blend mode',
    description='Which blend mode should be used. 0: Opaque, 1: Alpha, 2: Additive',
    default=0,
    min=0,
    max=5,
    update=OnTexture01Changed)

Material.num_textures = IntProperty(
    name='NumTextures',
    description='TODO',
    default=1,
    min=1,
    max=2,
    update=OnTexture01Changed)

Material.texture_path = StringProperty(
    name='texture path',
    description='Path to find the required texture',
    default='')

Material.texture_0 = StringProperty(
    name='Texture 0',
    description='TODO',
    default='',
    update=OnTexture01Changed)

Material.texture_1 = StringProperty(
    name='Texture 1',
    description='TODO',
    default='',
    update=OnTexture01Changed)



Material.bump_uv_scale = FloatVectorProperty(
    name='Bump UV Scale',
    subtype='TRANSLATION',
    size=2,
    default=(0.0, 0.0),
    min=0.0, max=1.0,
    description='Bump uv scale')

Material.edge_fade_out = FloatProperty(
    name='Edge fade out',
    description='TODO',
    default=0,
    min=0,
    max=5)

Material.depth_write = BoolProperty(
    name='Depth write',
    description='Todo',
    default=False)

Material.sampler_clamp_uv_no_mip_0 = FloatVectorProperty(
    name='Sampler clamp UV no MIP 0',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description='Sampler clampU clampV no mipmap 0')

Material.sampler_clamp_uv_no_mip_1 = FloatVectorProperty(
    name='Sampler clamp UV no MIP 1',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description='Sampler clampU clampV no mipmap 1')

def OnDiffuseTextureChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.diffuse_texture)
    self.node_tree.links.new(tex_node.outputs["Color"], principled.node_principled_bsdf.inputs["Base Color"])
Material.diffuse_texture = StringProperty(
    name='Diffuse Texture',
    description='The main color texture',
    default='',
    update=OnDiffuseTextureChanged)

def OnSpecTextureChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.spec_texture)
    spec_sepa_node = create_node_no_repeative(self, "ShaderNodeSeparateColor", "spec_sepa_node")
    self.node_tree.links.new(tex_node.outputs["Color"], spec_sepa_node.inputs["Color"])
    self.node_tree.links.new(spec_sepa_node.outputs["Red"], principled.node_principled_bsdf.inputs["Specular"])
    self.node_tree.links.new(spec_sepa_node.outputs["Green"], principled.node_principled_bsdf.inputs["Sheen"])
    self.node_tree.links.new(spec_sepa_node.outputs["Blue"], principled.node_principled_bsdf.inputs["Clearcoat"])
Material.spec_texture = StringProperty(
    name='Specular Texture',
    description='R channel: defines Specular Intensity; G channel: defines glassness; B channel: defines faction color position',
    default='',
    update=OnSpecTextureChanged)

def OnNrmTextureChanged(self:Material, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.normal_texture)

    separate_rgb = create_node_no_repeative(self, "ShaderNodeSeparateColor", "separate_rgb")
    self.node_tree.links.new(tex_node.outputs['Color'], separate_rgb.inputs['Color'])

    # 计算 X^2
    math_x2 = create_node_no_repeative(self, 'ShaderNodeMath', "math_x2")
    math_x2.operation = 'POWER'
    math_x2.inputs[1].default_value = 2.0
    self.node_tree.links.new(separate_rgb.outputs['Red'], math_x2.inputs[0])

    # 计算 Y^2
    math_y2 = create_node_no_repeative(self, 'ShaderNodeMath', "math_y2")
    math_y2.operation = 'POWER'
    math_y2.inputs[1].default_value = 2.0
    self.node_tree.links.new(separate_rgb.outputs['Green'], math_y2.inputs[0])

    # 计算 X^2 + Y^2
    math_add = create_node_no_repeative(self, 'ShaderNodeMath', "math_add")
    math_add.operation = 'ADD'
    self.node_tree.links.new(math_x2.outputs['Value'], math_add.inputs[0])
    self.node_tree.links.new(math_y2.outputs['Value'], math_add.inputs[1])

    # 计算 1 - (X^2 + Y^2)
    math_subtract = create_node_no_repeative(self, 'ShaderNodeMath', "math_subtract")
    math_subtract.operation = 'SUBTRACT'
    math_subtract.inputs[0].default_value = 1.0
    self.node_tree.links.new(math_add.outputs['Value'], math_subtract.inputs[1])

    # 计算 sqrt(1 - X^2 - Y^2)
    math_sqrt = create_node_no_repeative(self, 'ShaderNodeMath', "math_sqrt")
    math_sqrt.operation = 'SQRT'
    self.node_tree.links.new(math_subtract.outputs['Value'], math_sqrt.inputs[0])

    # 组合 X, Y, Z 通道为向量
    combine_rgb = create_node_no_repeative(self, 'ShaderNodeCombineRGB', "combine_rgb")
    self.node_tree.links.new(separate_rgb.outputs['Red'], combine_rgb.inputs['R'])  # X
    self.node_tree.links.new(separate_rgb.outputs['Green'], combine_rgb.inputs['G'])  # Y
    self.node_tree.links.new(math_sqrt.outputs['Value'], combine_rgb.inputs['B'])  # Z

    nrm_node = create_node_no_repeative(self, "ShaderNodeNormalMap", "nrm_node")
    self.node_tree.links.new(combine_rgb.outputs['Image'], nrm_node.inputs["Color"])
    self.node_tree.links.new(nrm_node.outputs["Normal"], principled.node_principled_bsdf.inputs["Normal"])

Material.normal_texture = StringProperty(
    name='Normal Map',
    description='The normal map texture. Only the R and G channels are used, representing the X and Y components of the normal vector. The Z component is reconstructed automatically.',
    default='',
    update=OnNrmTextureChanged)

def OnDamagedViewChanged(self:Material, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    if self.preview_holes and self.damaged_texture!="":
        damage_tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.damaged_texture)
        damage_tex_uv_node = create_node_no_repeative(self, "ShaderNodeUVMap", "damage_tex_uv_node")
        damage_tex_uv_node.uv_map = "UVMap.001"
        self.node_tree.links.new(damage_tex_uv_node.outputs['UV'], damage_tex_node.inputs['Vector'])
        self.node_tree.links.new(damage_tex_node.outputs["Alpha"], principled.node_principled_bsdf.inputs["Alpha"])
        self.blend_method = "HASHED"
    else:
        inputs = principled.node_principled_bsdf.inputs["Alpha"]
        if inputs.is_linked:
            link = inputs.links[0]
            self.node_tree.links.remove(link)
        self.blend_method = "OPAQUE"

Material.preview_holes = BoolProperty(
    name='Preview Damaged Model',
    description='Preview holes on the model by showing damaged texture',
    default=False,
    update=OnDamagedViewChanged
)

Material.damaged_texture = StringProperty(
    name='Damaged Texture',
    description='This texture works with the second uv map. In game, once a certain contact point bone is hit, the bounded surfaces will gain additional alpha according to this texture and the 2nd UV map. The positions of holes will become transprent.',
    default='',
    update=OnDamagedViewChanged)




Material.secondary_texture_blend_mode = IntProperty(
    name='Secondary texture blend mode',
    description='TODO',
    default=0,
    min=0,
    max=3)

Material.tex_coord_mapper_0 = IntProperty(
    name='TexCoord mapper 0',
    description='TODO',
    default=0,
    min=0,
    max=5)

Material.tex_coord_mapper_1 = IntProperty(
    name='TexCoord mapper 1',
    description='TODO',
    default=0,
    min=0,
    max=5)

Material.tex_coord_transform_0 = FloatVectorProperty(
    name='TexCoord transform 0',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description='TODO')

Material.tex_coord_transform_1 = FloatVectorProperty(
    name='TexCoord transform 1',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description='TODO')

Material.environment_texture = StringProperty(
    name='Environment texture',
    description='TODO',
    default='')

Material.environment_mult = FloatProperty(
    name='Environment mult',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

def OnBumpScaleChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    principled.normalmap_strength = self.bump_scale
Material.bump_scale = FloatProperty(
    name='Bump Scale',
    default=1.0,
    min=0.0, max=10.0,
    description='Additional Multiplier for the normal map value',
    update=OnBumpScaleChanged)

Material.recolor_texture = StringProperty(
    name='Recolor texture',
    description='TODO',
    default='')

Material.recolor_mult = FloatProperty(
    name='Recolor mult',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.use_recolor = BoolProperty(
    name='Use recolor colors',
    description='Enable faction color. Where to paint the color is defined in the alpha channel(defaultw3d, basicw3d, infantry)',
    default=False)

Material.use_world = BoolProperty(
    name='Use world cords',
    description='Todo',
    default=True)

Material.house_color_pulse = BoolProperty(
    name='House color pulse',
    description='Todo',
    default=False)

Material.scrolling_mask_texture = StringProperty(
    name='Scrolling mask texture',
    description='TODO',
    default='')

Material.tex_coord_transform_angle = FloatProperty(
    name='Texture coord transform angle',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_u_0 = FloatProperty(
    name='Texture coord transform u 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_v_0 = FloatProperty(
    name='Texture coord transform v 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_u_1 = FloatProperty(
    name='Texture coord transform u 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_v_1 = FloatProperty(
    name='Texture coord transform v 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_u_2 = FloatProperty(
    name='Texture coord transform u 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_coord_transform_v_2 = FloatProperty(
    name='Texture coord transform v 0',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

Material.tex_ani_fps_NPR_lastFrame_frameOffset_0 = FloatVectorProperty(
    name='TextureAnimation FPS NumPerRow LastFrame FrameOffset 0',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description='TODO')

Material.ion_hull_texture = StringProperty(
    name='Ion hull texture',
    description='TODO',
    default='')

Material.multi_texture_enable = BoolProperty(
    name='Multi texture enable',
    description='Todo',
    default=False)

# already existing
# Material.specular_color
# Material.specular_intensity
# Material.use_backface_culling
# Material.blend_method

