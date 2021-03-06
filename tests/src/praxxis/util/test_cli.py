from src.praxxis.util import cli
from tests.src.praxxis.util import dummy_object

def test_command(setup, 
         add_test_library, 
         init_root, 
         library_root, 
         library_db,
         output_root,
         scene_root,
         history_db,
         telemetry_db,
         rulesengine_root,
         rulesengine_db,
         model_root,
         model_db,
         default_scene_name,
         current_scene_db,
         query_start,
         query_end):
    import os
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.notebook import list_notebook
    from src.praxxis.notebook import run_notebook
    from src.praxxis.parameter import list_param
    from src.praxxis.notebook import open_notebook
    from src.praxxis.notebook import search_notebook
    from src.praxxis.scene import history
    from src.praxxis.notebook import add_notebook
    from src.praxxis.notebook import remove_notebook
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import end_scene
    from src.praxxis.scene import change_scene
    from src.praxxis.scene import resume_scene
    from src.praxxis.scene import delete_scene
    from src.praxxis.scene import list_scene
    from src.praxxis.library import add_library 
    from src.praxxis.library import remove_library 
    from src.praxxis.library import list_library 
    from src.praxxis.parameter import delete_param
    from src.praxxis.parameter import set_param
    from src.praxxis.parameter import list_param
    from src.praxxis.parameter import pull_param
    from src.praxxis.library import sync_library
    from src.praxxis.telemetry import update_settings 


    list_notebook.list_notebook(library_db, current_scene_db, query_start, query_end)

    dummy_input = dummy_object.make_dummy_input("run_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    sqlite_scene.clear_history(current_scene_db)
    assert result.__class__ == run_notebook.run_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("view_notebook_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_param.list_notebook_param.__class__

    dummy_input = dummy_object.make_dummy_input("open_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == open_notebook.open_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("search_notebooks")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == search_notebook.search_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("list_notebooks")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_notebook.list_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("history")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == history.history.__class__

    dummy_input = dummy_object.make_dummy_input("add_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == add_notebook.add_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("remove_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == remove_notebook.remove_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("new_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == new_scene.new_scene.__class__

    dummy_input = dummy_object.make_dummy_input("end_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == end_scene.end_scene.__class__

    dummy_input = dummy_object.make_dummy_input("change_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == change_scene.change_scene.__class__

    dummy_input = dummy_object.make_dummy_input("resume_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == resume_scene.resume_scene.__class__

    dummy_input = dummy_object.make_dummy_input("delete_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == delete_scene.delete_scene.__class__

    dummy_input = dummy_object.make_dummy_input("list_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_scene.list_scene.__class__

    dummy_input = dummy_object.make_dummy_input("add_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == add_library.add_library.__class__

    dummy_input = dummy_object.make_dummy_input("remove_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == remove_library.remove_library.__class__

    dummy_input = dummy_object.make_dummy_input("list_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_library.list_library.__class__

    dummy_input = dummy_object.make_dummy_input("set_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == set_param.set_param.__class__

    dummy_input = dummy_object.make_dummy_input("delete_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == delete_param.delete_parameter.__class__

    dummy_input = dummy_object.make_dummy_input("list_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_param.list_param.__class__

    dummy_input = dummy_object.make_dummy_input("view_library_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == list_param.list_library_param.__class__

    dummy_input = dummy_object.make_dummy_input("pull_notebook_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == pull_param.pull_notebook_parameter.__class__

    dummy_input = dummy_object.make_dummy_input("pull_library_param")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == pull_param.pull_library_parameter.__class__

    dummy_input = dummy_object.make_dummy_input("sync_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == sync_library.sync_library.__class__

    dummy_input = dummy_object.make_dummy_input("update_settings")
    result = cli.command(dummy_input, init_root, library_root, library_db, output_root, scene_root, history_db, telemetry_db, rulesengine_root, rulesengine_db, model_root, model_db, default_scene_name, True)
    assert result.__class__ == update_settings.update_settings.__class__
