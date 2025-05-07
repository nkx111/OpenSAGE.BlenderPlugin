import bpy
from bpy.props import *
from bpy.types import Material, PropertyGroup
from bpy_extras import node_shader_utils
from io_mesh_w3d.common.utils.helpers import *
from io_mesh_w3d.common.materials.RA3.parameter_map import *

inherited_texture_keys = ["texture_0", "diffuse_texture"]
def OnResetMaterialType(self:Material, context):
    if self.material_type != self.material_type_old:
        inherited_texture = ""
        _, para_map_old = get_material_parameter_map(self.material_type_old)
        _, para_map_new = get_material_parameter_map(self.material_type)
        for key, prop in self.bl_rna.properties.items():
            for tex_key in inherited_texture_keys:
                if key == tex_key and getattr(self, key) != "":
                    inherited_texture = getattr(self, key)
            if key in para_map_old.values() and not key in para_map_new.values():
                default = ""
                if hasattr(prop, "default"):
                    if hasattr(prop, "is_array") and getattr(prop, "is_array", False):
                        default = prop.default_array
                    else:
                        default = prop.default
                setattr(self, key, default)
        self.node_tree.nodes.clear()

        if inherited_texture != "":
            for tex_key in inherited_texture_keys:
                if tex_key in para_map_new.values():
                    setattr(self, tex_key, inherited_texture)

        self.name = self.name.replace(self.material_type_old, self.material_type)
        self.material_type_old = self.material_type

Material.material_type = EnumProperty(
    name='Material Type',
    description='defines the type of the material',
    items=material_type_items,
    default='DefaultW3D',
    update=OnResetMaterialType)

Material.material_type_old = EnumProperty(
    name='Material Type Old',
    description='defines the type of the material',
    items=material_type_items,
    default='DefaultW3D')

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
    description='The index of the technique (defined in the shader) to be used for rendering.',
    default=0,
    min=0,
    max=5)





def OnRenderingChanged(self:Material, context):
    if self.material_type in ["DefaultW3D", "Infantry", "Tree", "BasicW3D"]:
        if self.blend_mode == 0 and self.texture_0 != "" and self.texture_1 != "" and self.num_textures == 2:
            self.blend_method = "OPAQUE"
        else:
            if self.alpha_test == False:
                self.blend_method = "BLEND"    
                self.show_transparent_back = True
            else:
                self.blend_method = "CLIP"  
    elif self.material_type in ["MuzzleFlash","FXLightning","FXProtonCollider"]:
        self.blend_method = "BLEND"    
        self.show_transparent_back = True
    else:
        if self.alpha_test == False:
            self.blend_method = "OPAQUE"
        else:
            self.blend_method = "CLIP"  
            self.show_transparent_back = True


def OnTexture01Changed(self:Material, context):
    OnRenderingChanged(self,context)
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    if (self.num_textures == 1 or self.texture_1 == "" or self.material_type in ["MuzzleFlash", "FXLightning", "FXProtonCollider"]) and self.texture_0 != "":
        tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0, name="tex_node")
        uv_tex_0 = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_0")
        uv_tex_0.uv_map = "UVMap"
        mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
        x0,y0,vx,vy = self.tex_coord_transform_0
        mapping_tex_0.inputs["Scale"].default_value = (x0,y0,1)
        self.node_tree.links.new(uv_tex_0.outputs['UV'], mapping_tex_0.inputs['Vector'])
        self.node_tree.links.new(mapping_tex_0.outputs['Vector'], tex_node.inputs['Vector'])
        if self.material_type != "Infantry":
            if self.material_type == "MuzzleFlash":
                self.node_tree.links.new(tex_node.outputs["Alpha"], principled.node_principled_bsdf.inputs["Alpha"])
            else:
                if self.alpha_test:
                    math_node_alpha = create_node_no_repeative(self, "ShaderNodeMath", "math_node_alpha")
                    math_node_alpha.use_clamp = True
                    math_node_alpha.operation = 'MULTIPLY' 
                    math_node_alpha.inputs[1].default_value = self.alpha
                    self.node_tree.links.new(tex_node.outputs["Alpha"], math_node_alpha.inputs[0])
                    self.node_tree.links.new(math_node_alpha.outputs["Value"], principled.node_principled_bsdf.inputs["Alpha"])   
                else:
                    self.node_tree.links.new(tex_node.outputs["Color"], principled.node_principled_bsdf.inputs["Alpha"])
               

        color_mix_node_diffuse = create_node_no_repeative(self, "ShaderNodeMixRGB", "color_mix_node_diffuse")
        color_mix_node_diffuse.blend_type = 'MULTIPLY'
        color_mix_node_diffuse.inputs[0].default_value = 1  # Mix factor
        color_mix_node_diffuse.inputs[1].default_value = (*self.diffuse_color3, 1.0)  # Convert to 4D vector
        self.node_tree.links.new(tex_node.outputs["Color"], color_mix_node_diffuse.inputs[2])
        self.node_tree.links.new(color_mix_node_diffuse.outputs["Color"], principled.node_principled_bsdf.inputs["Base Color"])
        if self.material_type in ["FXLightning","FXProtonCollider"]:
            self.node_tree.links.new(color_mix_node_diffuse.outputs["Color"], principled.node_principled_bsdf.inputs["Emission"])
        
    elif self.texture_0 != "" and self.texture_1 != "" and self.num_textures == 2:
        tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0, name="tex_node")
        tex_node1 = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_1, name="tex_node1")

        texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
        texture_mix_node.blend_type = 'MULTIPLY'
        texture_mix_node.inputs[0].default_value = 0.5  # Mix factor
        self.node_tree.links.new(tex_node.outputs["Color"], texture_mix_node.inputs[1])
        self.node_tree.links.new(tex_node1.outputs["Color"], texture_mix_node.inputs[2])

        # opacity has no effect in w3d
        # math_node_alpha = create_node_no_repeative(self, "ShaderNodeMath", "math_node_alpha")
        # math_node_alpha.use_clamp = True
        # math_node_alpha.operation = 'MULTIPLY' 
        # math_node_alpha.inputs[1].default_value = self.alpha
        # self.node_tree.links.new(texture_mix_node.outputs["Color"], math_node_alpha.inputs[0])
        # self.node_tree.links.new(math_node_alpha.outputs["Value"], principled.node_principled_bsdf.inputs["Alpha"])
        if self.material_type != "Infantry":
            if self.alpha_test:
                math_node_alpha = create_node_no_repeative(self, "ShaderNodeMath", "math_node_alpha")
                math_node_alpha.use_clamp = True
                math_node_alpha.operation = 'MULTIPLY' 
                math_node_alpha.inputs[1].default_value = self.alpha
                self.node_tree.links.new(tex_node.outputs["Alpha"], math_node_alpha.inputs[0])
                self.node_tree.links.new(math_node_alpha.outputs["Value"], principled.node_principled_bsdf.inputs["Alpha"])   
            else:
                self.node_tree.links.new(texture_mix_node.outputs["Color"], principled.node_principled_bsdf.inputs["Alpha"])

        uv_tex_0 = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_0")
        uv_tex_0.uv_map = "UVMap"
        mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
        x0,y0,vx,vy = self.tex_coord_transform_0
        mapping_tex_0.inputs["Scale"].default_value = (x0,y0,1)
        self.node_tree.links.new(uv_tex_0.outputs['UV'], mapping_tex_0.inputs['Vector'])
        uv_tex_1 = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_1")
        uv_tex_1.uv_map = "UVMap.001"
        mapping_tex_1 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_1")
        x1,y1,vx,vy = self.tex_coord_transform_0
        mapping_tex_1.inputs["Scale"].default_value = (x1,y1,1)
        self.node_tree.links.new(uv_tex_1.outputs['UV'], mapping_tex_1.inputs['Vector'])

        self.node_tree.links.new(mapping_tex_0.outputs['Vector'], tex_node.inputs['Vector'])
        self.node_tree.links.new(mapping_tex_1.outputs['Vector'], tex_node1.inputs['Vector'])


        color_mix_node_diffuse = create_node_no_repeative(self, "ShaderNodeMixRGB", "color_mix_node_diffuse")
        color_mix_node_diffuse.blend_type = 'MULTIPLY'
        color_mix_node_diffuse.inputs[0].default_value = 1  # Mix factor
        color_mix_node_diffuse.inputs[1].default_value = (*self.diffuse_color3, 1.0)  # Convert to 4D vector
        self.node_tree.links.new(texture_mix_node.outputs["Color"], color_mix_node_diffuse.inputs[2])
        self.node_tree.links.new(color_mix_node_diffuse.outputs["Color"], principled.node_principled_bsdf.inputs["Base Color"])


Material.ambient_color3 = FloatVectorProperty(
    name='Ambient Color (RGB)',
    subtype='COLOR',
    size=3,
    default=(1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Color factor multiplied to the abmient light color. In Blender this option has no effect')

Material.ambient_color4 = FloatVectorProperty(
    name='Ambient Color (RGBA)',
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Color factor multiplied to the abmient light color. In Blender this option has no effect')

Material.diffuse_color4 = FloatVectorProperty(
    name='Diffuse Color (RGBA)',
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Diffuse color with alpha, only for shader BuildingsGenericDamageFill.fx. Not effect in Blender.')

Material.diffuse_color3 = FloatVectorProperty(
    name='Diffuse Color (RGB)',
    subtype='COLOR',
    size=3,
    default=(1.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='Color factor multiplied to the diffuse texture color',
    update=OnTexture01Changed)

def OnEmissionMultChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    principled.emission_strength = self.emission_mult


Material.emission_mult = FloatProperty(
    name='Emissive HDR Multipler',
    default=1.0,
    min=0.0, max=1000.0,
    description='Additional Multiplier for the Emission Color',
    update=OnEmissionMultChanged)

def OnEmissionColorChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    emission_color_node = create_node_no_repeative(self, "ShaderNodeRGB", "emission_color_node")
    emission_color_node.outputs["Color"].default_value = (*self.emission_color, 1.0)  # Convert to 4D vector
    self.node_tree.links.new(emission_color_node.outputs["Color"], principled.node_principled_bsdf.inputs["Emission"])
Material.emission_color = FloatVectorProperty(
    name='Emission Color',
    subtype='COLOR',
    size=3,
    default=(0, 0, 0),
    min=0.0, max=1.0,
    description='Emission color',
    update=OnEmissionColorChanged)

Material.alpha_test = BoolProperty(
    name='Alpha Test',
    description='Enable the alpha test. If true, Clip pixels with alpha < 96/255. Otherwise blend multiple objects with alpha',
    default=False,
    update=OnTexture01Changed)

def OnAlphaBlendChanged(self:Material, context):
    if self.alpha_blend:
        self.blend_mode=1
    else:
        self.blend_mode=0
Material.alpha_blend = BoolProperty(
    name='Alpha Blend',
    description='For Simple.fx: Which blend mode should be used. False: Opaque, True: Alpha',
    default=False,
    update=OnAlphaBlendChanged)

Material.alpha = FloatProperty(
    name='Alpha Multiplier',
    default=1.0,
    min=0.0, max=10.0,
    description='Additional Multiplier for the alpha value',
    update=OnTexture01Changed)

Material.blend_mode = IntProperty(
    name='Blend mode',
    description='Which blend mode should be used.\n0: Opaque\n1: Alpha\n2: Additive',
    default=0,
    min=0,
    max=5,
    update=OnRenderingChanged)

Material.num_textures = IntProperty(
    name='NumTextures',
    description='1: Use texture_0 only.\n2: Mix texture_0 and texture_1',
    default=2,
    min=1,
    max=2,
    update=OnTexture01Changed)

Material.texture_path = StringProperty(
    name='texture path',
    description='Path to find the required texture',
    default='')

Material.texture_0 = StringProperty(
    name='Texture 0',
    description='Base color texture for material type: DefaultW3D, Infantry, Tree and BasicW3D.\n* DefaultW3D: no alpha channel, texture color --> alpha.\n* Infantry: alpha channel represents faction color.\n* Tree and BasicW3D: alpha channel represents alpha' ,
    default='',
    update=OnTexture01Changed)

Material.texture_1 = StringProperty(
    name='Texture 1',
    description='DefaultW3D: To be mixed with Texture 0\nFXLightning: to be added to the uv of Texture_1.',
    default='',
    update=OnTexture01Changed)



def OnBumpScaleChanged(self, context):
    principled = node_shader_utils.PrincipledBSDFWrapper(self, is_readonly=False)
    principled.normalmap_strength = self.bump_uv_scale
Material.bump_uv_scale = FloatProperty(
    name='Bump Scale',
    default=1.0,
    min=0.0, max=10.0,
    description='Additional Multiplier for the normal map value',
    update=OnBumpScaleChanged)

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

Material.fog_enable = BoolProperty(
    name='Enable Fog',
    description='Used in simple.fx',
    default=True)

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
    self.node_tree.links.new(tex_node.outputs["Alpha"], principled.node_principled_bsdf.inputs["Alpha"])
Material.diffuse_texture = StringProperty(
    name='Diffuse Texture',
    description='The main color texture. No Alpha channel',
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

    # X^2
    math_x2 = create_node_no_repeative(self, 'ShaderNodeMath', "math_x2")
    math_x2.operation = 'POWER'
    math_x2.inputs[1].default_value = 2.0
    self.node_tree.links.new(separate_rgb.outputs['Red'], math_x2.inputs[0])

    # Y^2
    math_y2 = create_node_no_repeative(self, 'ShaderNodeMath', "math_y2")
    math_y2.operation = 'POWER'
    math_y2.inputs[1].default_value = 2.0
    self.node_tree.links.new(separate_rgb.outputs['Green'], math_y2.inputs[0])

    # X^2 + Y^2
    math_add = create_node_no_repeative(self, 'ShaderNodeMath', "math_add")
    math_add.operation = 'ADD'
    self.node_tree.links.new(math_x2.outputs['Value'], math_add.inputs[0])
    self.node_tree.links.new(math_y2.outputs['Value'], math_add.inputs[1])

    # 1 - (X^2 + Y^2)
    math_subtract = create_node_no_repeative(self, 'ShaderNodeMath', "math_subtract")
    math_subtract.operation = 'SUBTRACT'
    math_subtract.inputs[0].default_value = 1.0
    self.node_tree.links.new(math_add.outputs['Value'], math_subtract.inputs[1])

    # sqrt(1 - X^2 - Y^2)
    math_sqrt = create_node_no_repeative(self, 'ShaderNodeMath', "math_sqrt")
    math_sqrt.operation = 'SQRT'
    self.node_tree.links.new(math_subtract.outputs['Value'], math_sqrt.inputs[0])

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


def ScrollUV_Tex0(self,context):
    x0,y0,vx,vy = self.tex_coord_transform_0

    value_node_0_x = create_node_no_repeative(self, "ShaderNodeValue", "value_node_0_x")
    value_node_0_x_driver = value_node_0_x.outputs['Value'].driver_add('default_value')
    value_node_0_x_driver.driver.type = 'SCRIPTED'
    value_node_0_x_driver.driver.expression = f'frame / 30 * {vx}'

    value_node_0_y = create_node_no_repeative(self, "ShaderNodeValue", "value_node_0_y")
    value_node_0_y_driver = value_node_0_y.outputs['Value'].driver_add('default_value')
    value_node_0_y_driver.driver.type = 'SCRIPTED'
    value_node_0_y_driver.driver.expression = f'frame / 30 * {-vy}' # need to invert y. Why?

    value_node_0_xyz = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "value_node_0_xyz")
    self.node_tree.links.new(value_node_0_x.outputs['Value'], value_node_0_xyz.inputs['X'])
    self.node_tree.links.new(value_node_0_y.outputs['Value'], value_node_0_xyz.inputs['Y'])

    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    self.node_tree.links.new(value_node_0_xyz.outputs['Vector'], mapping_tex_0.inputs['Location'])

    texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
    texture_mix_node.inputs[0].default_value = 1

def UnScrollUV_Tex0(self, context):
    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    inputs = mapping_tex_0.inputs["Location"]
    if inputs.is_linked:
        link = inputs.links[0]
        self.node_tree.links.remove(link)
    texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
    texture_mix_node.inputs[0].default_value = 0.5

def ScrollUV_Tex1(self,context):
    x1,y1,vx,vy = self.tex_coord_transform_1

    value_node_1_x = create_node_no_repeative(self, "ShaderNodeValue", "value_node_1_x")
    value_node_1_x_driver = value_node_1_x.outputs['Value'].driver_add('default_value')
    value_node_1_x_driver.driver.type = 'SCRIPTED'
    value_node_1_x_driver.driver.expression = f'frame / 30 * {vx}'

    value_node_1_y = create_node_no_repeative(self, "ShaderNodeValue", "value_node_1_y")
    value_node_1_y_driver = value_node_1_y.outputs['Value'].driver_add('default_value')
    value_node_1_y_driver.driver.type = 'SCRIPTED'
    value_node_1_y_driver.driver.expression = f'frame / 30 * {-vy}'

    value_node_1_xyz = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "value_node_1_xyz")
    self.node_tree.links.new(value_node_1_x.outputs['Value'], value_node_1_xyz.inputs['X'])
    self.node_tree.links.new(value_node_1_y.outputs['Value'], value_node_1_xyz.inputs['Y'])

    mapping_tex_1 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_1")
    self.node_tree.links.new(value_node_1_xyz.outputs['Vector'], mapping_tex_1.inputs['Location'])

    texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
    texture_mix_node.inputs[0].default_value = 1

def UnScrollUV_Tex1(self, context):
    mapping_tex_1 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_1")
    inputs = mapping_tex_1.inputs["Location"]
    if inputs.is_linked:
        link = inputs.links[0]
        self.node_tree.links.remove(link)
    texture_mix_node = create_node_no_repeative(self, "ShaderNodeMixRGB", "texture_mix_node")
    texture_mix_node.inputs[0].default_value = 0.5

# MuzzleFlash
def ScrollAndRotateUV_Muzzle(self, context):
    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    mapping_tex_0.inputs["Location"].default_value = (-self.tex_coord_trans_u0, -self.tex_coord_trans_v0, 0)

    value_node_rotate = create_node_no_repeative(self, "ShaderNodeValue", "value_node_rotate")
    value_node_rotate_driver = value_node_rotate.outputs['Value'].driver_add('default_value')
    value_node_rotate_driver.driver.type = 'SCRIPTED'
    if self.multi_texture_enable:
        value_node_rotate_driver.driver.expression = f'frame / 30 * {-self.tex_coord_trans_angle}'
    else:
        value_node_rotate_driver.driver.expression = f'frame / 30 * {self.tex_coord_trans_angle}'

    combine_node_rotate = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "combine_node_rotate")
    self.node_tree.links.new(value_node_rotate.outputs['Value'], combine_node_rotate.inputs['Z'])

    mapping_tex_0_rotate = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0_rotate")
    mapping_tex_0_rotate.inputs["Location"].default_value = (self.tex_coord_trans_u0, self.tex_coord_trans_v0, 0)
    self.node_tree.links.new(combine_node_rotate.outputs['Vector'], mapping_tex_0_rotate.inputs['Rotation'])
    self.node_tree.links.new(mapping_tex_0.outputs['Vector'], mapping_tex_0_rotate.inputs['Vector'])

    tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0, name="tex_node")
    self.node_tree.links.new(mapping_tex_0_rotate.outputs['Vector'], tex_node.inputs['Vector'])

def UnScrollAndRotateUV_Muzzle(self, context):
    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    mapping_tex_0.inputs["Location"].default_value = (0, 0, 0)
    tex_node = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_0, name="tex_node")
    self.node_tree.links.new(mapping_tex_0.outputs['Vector'], tex_node.inputs['Vector'])

# FXLightning
def ScrollAndRotateUV_Lightning(self, context):
    value_node_nrm = create_node_no_repeative(self, "ShaderNodeValue", "value_node_nrm_x")
    value_node_nrm_driver = value_node_nrm.outputs['Value'].driver_add('default_value')
    value_node_nrm_driver.driver.type = 'SCRIPTED'
    value_node_nrm_driver.driver.expression = f'frame / 30 * 0.01 * {self.disp_speed}'

    combine_node_nrm = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "combine_node_nrm")
    self.node_tree.links.new(value_node_nrm.outputs['Value'], combine_node_nrm.inputs['X'])

    uv_tex_nrm = create_node_no_repeative(self, "ShaderNodeUVMap", "uv_tex_nrm")
    uv_tex_nrm.uv_map = "UVMap"
    mapping_tex_nrm = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_nrm")
    self.node_tree.links.new(combine_node_nrm.outputs['Vector'], mapping_tex_nrm.inputs['Location'])
    self.node_tree.links.new(uv_tex_nrm.outputs['UV'], mapping_tex_nrm.inputs['Vector'])
    mapping_tex_nrm.inputs["Rotation"].default_value = (0, 0, self.disp_angle * 0.017453)
    mapping_tex_nrm.inputs["Scale"].default_value = (self.disp_scalar, self.disp_scalar, 1)

    tex_node_nrm = create_texture_node(self, context.preferences.addons["io_mesh_w3d"].preferences.texture_paths, self.texture_1, name="tex_node_nrm")
    self.node_tree.links.new(mapping_tex_nrm.outputs['Vector'], tex_node_nrm.inputs['Vector'])

    sep_color_nrm = create_node_no_repeative(self, "ShaderNodeSeparateColor", "sep_color_nrm")
    self.node_tree.links.new(tex_node_nrm.outputs['Color'], sep_color_nrm.inputs['Color'])

    combine_node_nrm_color = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "combine_node_nrm_color")
    self.node_tree.links.new(sep_color_nrm.outputs['Red'], combine_node_nrm_color.inputs['X'])
    self.node_tree.links.new(sep_color_nrm.outputs['Green'], combine_node_nrm_color.inputs['Y'])

    math_nrm = create_node_no_repeative(self, "ShaderNodeVectorMath", "math_nrm")
    math_nrm.operation = 'MULTIPLY' 
    self.node_tree.links.new(combine_node_nrm_color.outputs['Vector'], math_nrm.inputs[0])
    math_nrm.inputs[1].default_value = (self.disp_amp, self.disp_amp, 0)

    vx, vy, sx, sy = self.diffuse_coord_offset

    value_node_diffuse_x = create_node_no_repeative(self, "ShaderNodeValue", "value_node_diffuse_x")
    value_node_diffuse_x_driver = value_node_diffuse_x.outputs['Value'].driver_add('default_value')
    value_node_diffuse_x_driver.driver.type = 'SCRIPTED'
    value_node_diffuse_x_driver.driver.expression = f'frame / 30 * {vx}'

    value_node_diffuse_y = create_node_no_repeative(self, "ShaderNodeValue", "value_node_diffuse_y")
    value_node_diffuse_y_driver = value_node_diffuse_y.outputs['Value'].driver_add('default_value')
    value_node_diffuse_y_driver.driver.type = 'SCRIPTED'
    value_node_diffuse_y_driver.driver.expression = f'frame / 30 * {vy}'

    combine_node_diffuse = create_node_no_repeative(self, "ShaderNodeCombineXYZ", "combine_node_diffuse")
    self.node_tree.links.new(value_node_diffuse_x.outputs['Value'], combine_node_diffuse.inputs['X'])
    self.node_tree.links.new(value_node_diffuse_y.outputs['Value'], combine_node_diffuse.inputs['Y'])

    math_nrm_diffuse = create_node_no_repeative(self, "ShaderNodeVectorMath", "math_nrm_diffuse")
    math_nrm_diffuse.operation = 'ADD' 
    self.node_tree.links.new(math_nrm.outputs['Vector'], math_nrm_diffuse.inputs[0])   
    self.node_tree.links.new(combine_node_diffuse.outputs['Vector'], math_nrm_diffuse.inputs[1])   

    # retrieve
    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    self.node_tree.links.new(math_nrm_diffuse.outputs['Vector'], mapping_tex_0.inputs["Location"])   
    mapping_tex_0.inputs["Scale"].default_value = (sx, sy, 1)


def UnScrollAndRotateUV_Lightning(self, context):
    # retrieve
    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    inputs = mapping_tex_0.inputs["Location"]
    if inputs.is_linked:
        link = inputs.links[0]
        self.node_tree.links.remove(link)
    mapping_tex_0.inputs["Scale"].default_value = (1, 1, 1)


def OnScrollUV(self: Material, context):
    x0,y0,vx,vy = self.tex_coord_transform_0
    x1,y1,vx,vy = self.tex_coord_transform_1

    mapping_tex_0 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_0")
    mapping_tex_1 = create_node_no_repeative(self, "ShaderNodeMapping", "mapping_tex_1")

    mapping_tex_0.inputs["Scale"].default_value = (x0,y0,1)
    mapping_tex_1.inputs["Scale"].default_value = (x1,y1,1)

    if self.material_type == "MuzzleFlash":
        if self.preview_scrolling:
            ScrollAndRotateUV_Muzzle(self,context)
        else:
            UnScrollAndRotateUV_Muzzle(self,context)
    elif self.material_type in ["FXLightning","FXProtonCollider"]:
        if self.preview_scrolling:
            ScrollAndRotateUV_Lightning(self,context)
        else:
            UnScrollAndRotateUV_Lightning(self,context)
    else:
        if self.tex_coord_mapper_0 == 1 and self.preview_scrolling:
            ScrollUV_Tex0(self, context)
        else:
            UnScrollUV_Tex0(self,context)

        if self.tex_coord_mapper_1 == 1 and self.preview_scrolling:
            ScrollUV_Tex1(self, context)
        else:
            UnScrollUV_Tex1(self,context)

Material.secondary_texture_blend_mode = IntProperty(
    name='Secondary texture blend mode',
    description='Affects color blend mode for the secondary texture. No effect here in Blender.\n0: multiply.\n1: multiply and then multiply by 2.\n2: mix with texture_0 alpha.\n3: do not use texture_1, but accumulate SpecularColor',
    default=0,
    min=0,
    max=3)

Material.tex_coord_mapper_0 = IntProperty(
    name='TexCoord mapper 0',
    description='Controls uv scrolling of texture_0. 0: No scroll. 1: scroll. 2: video-like scroll',
    default=0,
    min=0,
    max=2,
    update=OnScrollUV)

Material.tex_coord_mapper_1 = IntProperty(
    name='TexCoord mapper 1',
    description='Controls uv scrolling of texture_1. 0: No scroll. 1: scroll.',
    default=0,
    min=0,
    max=1,
    update=OnScrollUV)

Material.tex_coord_transform_0 = FloatVectorProperty(
    name='TexCoord transform 0',
    subtype='TRANSLATION',
    size=4,
    default=(1.0, 1.0, 0.0, 0.0),
    min=-100.0, max=100.0,
    description='Defines scroll parameters of texture_0. x,y: scale. z,w: scroll speed per second',
    update=OnScrollUV)

Material.tex_coord_transform_1 = FloatVectorProperty(
    name='TexCoord transform 1',
    subtype='TRANSLATION',
    size=4,
    default=(1.0, 1.0, 0.0, 0.0),
    min=-100.0, max=100.0,
    description='Defines scroll parameters of texture_1. x,y: scale. z,w: scroll speed per second',
    update=OnScrollUV)

Material.preview_scrolling = BoolProperty(
    name='Preview Texture Scrolling',
    description='Simulate the scrolling effect of textures. Press Space-key to start animation, the uv coordinates will change with time.',
    default=False,
    update=OnScrollUV)

Material.environment_texture = StringProperty(
    name='Environment texture',
    description='TODO',
    default='')

Material.environment_mult = FloatProperty(
    name='Environment mult',
    default=0.0,
    min=0.0, max=1.0,
    description='Todo')

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
    description='Use world coordinates to scroll the textures, instead of time. No effect in Blender.',
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
    name='MultiTextureEnable',
    description='In FXLightning: Sample Texture_0 for a second time using inversed uv displacement. No effect in Blender\nIn MuzzleFlash: Revert rotation direction.',
    default=False,
    update=OnScrollUV)

Material.diffuse_coord_offset = FloatVectorProperty(
    name='DiffuseCoordOffset',
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 1.0, 1.0),
    min=0.0, max=1.0,
    description='In FXLightning: UV scroll parameters of Texture_0. x,y: scroll speed. z,w: scaling',
    update=OnScrollUV)

Material.multiply_blend_enable = BoolProperty(
    name='MultiplyBlendEnable',
    description='Todo',
    default=False)

Material.unique_coord_scalar = FloatProperty(
    name='UniqueWorldCoordScalar',
    default=0.0,
    min=0.0, max=1.0,
    description='Multiplied to the world coordinates when using world coordinates as UV. No effect in Blender.')

Material.unique_coord_strength = FloatProperty(
    name='UniqueWorldCoordStrength',
    default=0.0,
    min=0.0, max=1.0,
    description='Same as UniqueWorldCoordScalar (stupid EA code...). No effect in Blender.')

Material.disp_scalar = FloatProperty(
    name='DisplaceScalar',
    default=0.0,
    min=0.0, max=50.0,
    description='UV scale factor for Texture_1',
    update=OnScrollUV)

Material.disp_amp = FloatProperty(
    name='DisplaceAmp',
    default=0.0,
    min=0.0, max=50.0,
    description='Additional amplitude for the Texture_1 sampling result.',
    update=OnScrollUV)

Material.disp_angle = FloatProperty(
    name='DisplaceDivergenceAngle',
    default=0.0,
    min=0.0, max=180.0,
    description='UV rotation angle for Texture_1',
    update=OnScrollUV)

Material.disp_speed = FloatProperty(
    name='DisplaceSpeed',
    default=0.0,
    min=0.0, max=50.0,
    description='UV scrolling speed for Texture_1. Scroll x only',
    update=OnScrollUV)




Material.tex_coord_trans_angle = FloatProperty(
    name='Rotation Speed',
    default=1.0,
    min=-100.0, max=100.0,
    description='Texture UV rotation speed',
    update=OnScrollUV)

Material.tex_coord_trans_u0 = FloatProperty(
    name='Texture UV Offset: U0',
    default=0.5,
    min=0.0, max=1.0,
    description='Texture UV rotation center',
    update=OnScrollUV)

Material.tex_coord_trans_v0 = FloatProperty(
    name='Texture UV Offset: V0',
    default=0.5,
    min=0.0, max=1.0,
    description='Texture UV rotation center',
    update=OnScrollUV)

Material.tex_coord_trans_u1 = FloatProperty(
    name='Texture UV Offset: U1',
    default=0.5,
    min=0.0, max=1.0,
    description='Another rotation center under differnt VertexColor. No effect?')

Material.tex_coord_trans_v1 = FloatProperty(
    name='Texture UV Offset: V1',
    default=0.5,
    min=0.0, max=1.0,
    description='Another rotation center under differnt VertexColor. No effect?')

Material.tex_coord_trans_u2 = FloatProperty(
    name='Texture UV Offset: U2',
    default=0.5,
    min=0.0, max=1.0,
    description='Another rotation center under differnt VertexColor. No effect?')

Material.tex_coord_trans_v2 = FloatProperty(
    name='Texture UV Offset: V2',
    default=0.5,
    min=0.0, max=1.0,
    description='Another rotation center under differnt VertexColor. No effect?')



# already existing
# Material.specular_color
# Material.specular_intensity
# Material.use_backface_culling
# Material.blend_method
# Material.metallic

Material.specular_intensity2 = FloatProperty(
    name='Shiness',
    default=1.0,
    min=0.0, max=50.0,
    description='Additional multiplier for the Specular Color. No effect in PBR. No effect in Blender. Please set to 1.')

Material.specular_color2 = FloatVectorProperty(
    name='Specular Color',
    subtype='COLOR',
    size=3,
    default=(0, 0, 0),
    min=0.0, max=1.0,
    description='Color factor multiplied to the reflected color component. No effect in PBR. No effect in Blender. Please set to 0.')