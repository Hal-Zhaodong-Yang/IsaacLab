import omni.isaac.urdf
urdf_interface = omni.isaac.urdf.acquire_urdf_interface()
urdf_interface.import_robot(
    "/home/zyang645/RobotLearning/code/Kinova_Ability_Allegro/src/ros_kortex/kortex_description/arms/gen3/7dof/urdf/GEN3-7DOF-VISION_ARM_WITH_ALLEGRO_URDF.urdf")