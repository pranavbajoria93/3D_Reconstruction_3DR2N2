import bpy
import os

count=0
for root, dirs, files in os.walk(r"/home/vguduru1/3D-R2N2/ShapeNet/ShapeNetObj/04090263"):
    for file in files:
        if file.endswith(".obj"):
            count+=1

i=0
for root, dirs, files in os.walk(r"/home/vguduru1/3D-R2N2/ShapeNet/ShapeNetObj/04090263"):
    for file in files:
        if file.endswith(".obj"):
            print('folder in progress',root)
            print('rendering {} file'.format(i),root)
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete(use_global=False)
            bpy.ops.object.light_add(type='SUN', location=(5, 5, 2.5))
            bpy.context.active_object.name = 'SUN11'
            bpy.data.objects['SUN11'].field.strength=10
            bpy.ops.object.light_add(type='SUN', location=(-5, 5, 2.5))
            bpy.context.active_object.name = 'SUN01'
            bpy.data.objects['SUN01'].field.strength=10
            bpy.ops.object.light_add(type='SUN', location=(-5, -5, 2.5))
            bpy.context.active_object.name = 'SUN00'
            bpy.data.objects['SUN00'].field.strength=10
            bpy.ops.object.light_add(type='SUN', location=(5, -5, 2.5))
            bpy.context.active_object.name = 'SUN10'
            bpy.data.objects['SUN10'].field.strength=10
            bpy.ops.mesh.primitive_monkey_add(size=2, enter_editmode=False, location=(0, 0, 0))
            bpy.context.active_object.name = 'Recon'
            bpy.context.object.scale[0] = 0.01
            bpy.context.object.scale[1] = 0.01
            bpy.context.object.scale[2] = 0.01

            bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(1, 1, 1), rotation=(1.10871, 0.0E132652, 1.14827))
            bpy.context.active_object.name = 'Camera'
            bpy.ops.object.constraint_add(type='TRACK_TO')
            bpy.context.object.constraints["Track To"].target = bpy.data.objects["Recon"]
            bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
            bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
            bpy.ops.object.location_clear(clear_delta=False)
            bpy.ops.object.rotation_clear(clear_delta=False)
            bpy.ops.curve.primitive_bezier_circle_add(radius=2, enter_editmode=False, location=(0, 0, 0))
            bpy.ops.object.empty_add(type='CUBE', location=(0, 0, 0))
            bpy.context.active_object.name = 'Cube'


            a=bpy.data.objects['Camera']
            b=bpy.data.objects['Cube']
            a.parent=b
            bpy.ops.collection.create()
            bpy.data.objects['Cube'].select_set(True)
            bpy.ops.object.constraint_add(type='FOLLOW_PATH')
            bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["BezierCircle"]
            bpy.context.object.constraints["Follow Path"].use_fixed_location = True
            bpy.context.object.constraints["Follow Path"].use_curve_follow = True
            bpy.context.object.constraints["Follow Path"].up_axis = 'UP_Z'
            bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_Y'
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)

            #bpy.ops.object.location_clear(clear_delta=False)
            #bpy.ops.object.rotation_clear(clear_delta=False)

            bpy.ops.transform.translate(value=(0,0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

            scene=bpy.context.scene
            scene.frame_start=1
            scene.frame_end=510

            ##Round -1
            f=-1
            frame_num=1
            ob=bpy.data.objects["Cube"]
            cam=bpy.data.objects['Camera']

            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)
            frame_num+=50
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.25
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            frame_num+=50
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.5
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, 2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            frame_num+=50
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.75
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            frame_num+=50
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 1
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, 2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            frame_num+=50
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            ##Round-2
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.05
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            frame_num+=5
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            frame_num+=50
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.25
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, 2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            frame_num+=50
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.5
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            frame_num+=50
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 0.75
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, 2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            frame_num+=50
            bpy.context.scene.frame_set(frame_num)
            bpy.context.object.constraints["Follow Path"].offset_factor = 1
            bpy.data.objects['Cube'].select_set(False)
            bpy.data.objects['Camera'].select_set(True)
            bpy.ops.transform.translate(value=(0,0, -2), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            cam.keyframe_insert(data_path='location',frame=frame_num)
            ob.keyframe_insert(data_path='constraints["Follow Path"].offset_factor',frame=frame_num)

            scn = bpy.context.scene
            scn.render.engine = 'CYCLES'
            scn.world.use_nodes = True
            wd = scn.world
            nt = bpy.data.worlds[wd.name].node_tree
            gradNode = nt.nodes.new(type="ShaderNodeTexGradient")
            backNode = nt.nodes['Background']
            gradNode.location.x = backNode.location.x
            gradNode.location.y = backNode.location.y
            gradColOut = gradNode.outputs['Color']
            backColIn = backNode.inputs['Color']
            nt.links.new(gradColOut, backColIn)
            gradNode.gradient_type = 'EASING'
            bpy.context.scene.render.resolution_x = 127
            bpy.context.scene.render.resolution_y = 127
            bpy.context.scene.frame_step=10
            bpy.context.scene.render.image_settings.file_format = 'AVI_JPEG'
            bpy.context.scene.render.image_settings.color_mode = 'RGB'
            bpy.context.scene.render.image_settings.quality = 50
            bpy.context.scene.camera = bpy.data.objects["Camera"]



                
                
            dir=os.path.join(root,file)
            bpy.ops.import_scene.obj(filepath=dir)
            
            
            folder = os.path.join(root, 'render')
            scene = bpy.context.scene
#                #scene.layers = [True] * 20 # Show all layers

            for obj in scene.objects:
                if obj.type == 'MESH':
                    bpy.context.view_layer.objects.active = obj
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
                    bpy.ops.object.editmode_toggle()

            
            
            folder = os.path.join(root,file)
            bpy.context.scene.render.filepath=folder
            bpy.ops.render.render(animation=True,use_viewport=True)


            i+=1
            print('completed rendering {} file'.format(i))
            
            
            print('Progress',i/count)
                
                

