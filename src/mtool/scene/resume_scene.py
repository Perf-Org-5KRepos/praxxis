"""
This file resumes a previously used scene.
"""

def resume_scene(args, scene_root, history_db):
    """Resumes a scene"""
    import os

    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.display import display_scene
    from src.mtool.scene import scene
    from src.mtool.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name
    try:
        sqlite_scene.check_scene_ended(history_db, name)
    except error.SceneNotFoundError as e:
        raise e

    scene = os.path.join(scene_root, name, f"{name}.db" )

    sqlite_scene.resume_scene(scene, name)
    sqlite_scene.mark_resumed_scene(history_db, name)
    sqlite_scene.update_current_scene(history_db, name)
    
    display_scene.display_resume_scene(name)
    return name
    