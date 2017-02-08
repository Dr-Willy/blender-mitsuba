#  __init__.py
#  date : 02/02/2017
# author: Laurent Boiron 
# 

# blender addon for mitsuba export

bl_info = {
    "name": "Mitsuba Tools",
    "description": "Tools for mitsuba",
    "author": "Laurent Boiron (INIRA/Graphdeco)",
    "version": (0, 1),
    "blender": (2, 78, 0),
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "category": "Export"
    }

import bpy
from . import camera

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()



