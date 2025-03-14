# AsymDex

### Building lab kinova robot setting in IsaacLab

#### Try IsaacSim robot assembly tool

- Successfully assembled kinova gen3 arm and allegro right hand in IsaacSim (*2025.03.02*)
  - Couldn't find Allegro left hand model in IsaacSim asset
  - Tried using the assembled .usd file in IsaacLab (based on [Articulation tutorial](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/01_assets/run_articulation.html)), replace the catpole model with our assembled model. Isaac Lab raised error (two prims in the .usd file error, must specify one, although I checked the "treat as a single robot" button while assembling)
  - DexPBT used a unified urdf file for Kuka arm and Allegro hand ([IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs/tree/main/assets/urdf/kuka_allegro_description)), maybe it's better to use a unified urdf file to convert to a usd file?
- Tried creating a urdf file containing both the arm and the hand (*2025.03.04*)
  - Kinova urdf from [ros_kortex](https://github.com/Kinovarobotics/ros_kortex) can be imported into IsaacSim
  - Allegro Hand model from [Bidexhand](https://github.com/PKU-MARL/DexterousHands) cannot be imported into IsaacSim
    - It turns out IsaacSim cannot read the .stl files of the Allegro hand mesh from Bidexhand (Strange). If replacing the .stl with .obj found in other github repo, IsaacSim can import it.
  - Find another useful [Allegro Hand repo](https://github.com/simlabrobotics/allegro_hand_ros/tree/master). The urdf can be imported into IsaacSim if the change the "." in the file name of the stl mesh (They are named like "link_0.0.STL" at the beginning, and IsaacSim cannot import them)
  - **Useful Online URDF viewer: [link](https://github.com/gkjohnson/urdf-loaders)**

#### Try importing the created urdf into IsaacGym

- The urdf can be imported, but the simulation of joint_pos_control doesn't work (some joint keeps spinning, simulation not converging) (*2025.3.10*)
  - Changed the IsaacGym asset dof prop, "armature" to 0.01 using `hand_arm_dof_props["armature"].fill(0.01)`, the simulation converged. But joint pos control still doesn't work well
  - Used another urdf and the simulation works fine. The arm part urdf is exactly the same. It seems the problem is the hand part? Maybe the inertia  or mass value is causing the first urdf file to be unstable.