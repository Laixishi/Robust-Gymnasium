import robust_gymnasium.envs.robosuite.macros as macros
from robust_gymnasium.envs.robosuite.models.base import MujocoXML
from robust_gymnasium.envs.robosuite.utils.mjcf_utils import convert_to_string, find_elements, xml_path_completion


class MujocoWorldBase(MujocoXML):
    """Base class to inherit all mujoco worlds from."""

    def __init__(self):
        super().__init__(xml_path_completion("base.xml"))
        # Modify the simulation timestep to be the requested value
        options = find_elements(root=self.root, tags="option", attribs=None, return_first=True)
        options.set("timestep", convert_to_string(macros.SIMULATION_TIMESTEP))
