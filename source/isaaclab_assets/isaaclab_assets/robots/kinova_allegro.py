import math

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

KINOVA_ALLEGRO_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"source/isaaclab_assets/data/Robots/Kinova/kinova_allegro_one_robot.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            enable_gyroscopic_forces=False,
            angular_damping=0.01,
            max_linear_velocity=1000.0,
            max_angular_velocity=64 / math.pi * 180.0,
            max_depenetration_velocity=5.0,
            max_contact_impulse=1e32,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
        ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.005, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        rot=(0.257551, 0.283045, 0.683330, -0.621782),
        joint_pos={"^(?!thumb_joint_0).*_joint_.*": 0.0, "thumb_joint_0": 0.28,
                   "joint_1": 0.0,
                    "joint_2": 0.65,
                    "joint_3": 0.0,
                    "joint_4": 1.89,
                    "joint_5": 0.0,
                    "joint_6": 0.6,
                    "joint_7": -1.57,},
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*_joint_.*"],
            effort_limit=0.5,
            velocity_limit=100.0,
            stiffness=3.0,
            damping=0.1,
            friction=0.01,
        ),
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["joint_[1-7]"],
            velocity_limit=100.0,
            effort_limit={
                "joint_[1-4]": 39.0,
                "joint_[5-7]": 9.0,
            },
            stiffness={
                "joint_[1-4]": 40.0,
                "joint_[5-7]": 15.0,
            },
            damping={
                "joint_[1-4]": 1.0,
                "joint_[5-7]": 0.5,
            },
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)