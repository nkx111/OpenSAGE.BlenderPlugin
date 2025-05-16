安装方法：blender(已测试3.6、4.0版本)中进入 `编辑-preferences-插件-install` 页面，选择这个zip（无需解压），点击导入后应用即可。
GitHub地址：https://github.com/nkx111/OpenSAGE.BlenderPlugin
使用教程：https://www.yuque.com/muzeqaq/zokrzi/tagc2i68590wsecy

功能：
导入各种C&C系列的模型，完美导出用于RA3的模型，无需启动max！
直接在Blender中预览DefaultW3D等材质特效，实时调节参数！
设置图片查找路径，一键更换贴图！

支持的RA3材质（Shader）：
"BuildingsSoviet", "BuildingsAllied", "BuildingsJapan", "BuildingsGeneric", "NormalMapped", "BuildingsGenericDamageFill","ObjectsSoviet", "ObjectsAllied", "ObjectsJapan", "ObjectsTerrain", "ObjectsAlliedTread", "ObjectsGeneric", "Infantry", "Tree", "BasicW3D", "DefaultW3D", "Simple", "Simplest", "TreeSway", "MuzzleFlash", "FXLightning", "FXProtonCollider"

使用说明：
1. 导入：文件-导入-w3d/w3x-选择文件。导入模型请选择 container 文件，一般带有 SKN 或者 CTR 的后缀。导入模型后再导入动画。
2. 导出：文件-导出-w3d/w3x。注意要选择格式为“Westwood 3D XML”，默认是“Westwood 3D Binary”。默认导出 mesh + hierarchy + container 到一个文件，也可以选择同时导出动画。不要选择导出单独的文件或网格。

注意事项：
1. 需要回到物体模式进行导出

暂时未实现：
1. 同时导入和管理多个动画
2. 动画透明度channel问题、多channel动画导出疑似存在异常

2025/5/16 更新：
修复了defaultw3d的uv缩放问题，不是所有选项都应用uv缩放
适配 blender 4.x 版本
新增了阵营色预览功能

2025/5/9 更新：
重写了材质的导入导出逻辑。现在能够支持所有RA3材质了，导出后的参数不会有异常。
可以在下拉列表里选择不同的材质，不同的材质会切换不同的属性面板。
添加了大量材质的预览，可以在编辑器中看到特效
可以设置图片查找路径，方便一键更换贴图
如果导入其他C&C的模型，会自动选择兼容的RA3材质。

2023/8/18 更新：
不再需要手动编辑导出的w3x文件。文件中不再生成include区块、贴图名称不再有奇怪的.dds后缀。
修复了重复导入时mesh异常的问题。
支持第二UVmap和DamagedTexture的fxshader属性。现在可以编辑建筑物的破损模型。
更好的自动搜索与导入功能。现在会自动搜索mesh所对应的CTR、CTR所对应的SKL。此外可以在模型本体导入完成后继续导入动画。




