"""
This file opens a notebook in Azure Data Studio.
"""

def open_notebook(args, current_scene_db, library_db, ads_location, editor, test = False):
    """Opens a notebook, by getting the filename and then opening from the ads binary location"""
    import subprocess
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.notebook import notebook
    from src.mtool.util import error

    name = args.notebook
    
    try:
        tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    except error.NotebookNotFoundError as e:
        raise e
    
    if tmp_name != None:
        name = tmp_name

    try:
        notebook_data = sqlite_notebook.get_notebook(library_db, name)
    except error.NotebookNotFoundError as e:
        raise e
    
    notebook_filename = notebook_data[0]
    if args.environment == "html":
        display_as_html(notebook_filename)
    elif args.environment == "jupyter":
        open_jupyter(notebook_filename, test)
    elif args.environment == "ads":
        subprocess.Popen([ads_location, notebook_filename])
    else:
        open_editor(notebook_filename, editor)
    return 0


def display_as_html(filename, html_outputfile = None):
    """opens the file as html in the web browser"""
    import nbconvert
    import webbrowser

    output = nbconvert.exporters.export(nbconvert.HTMLExporter(), filename)[0]
    if html_outputfile == None:
        import tempfile
        # create temporary file
        temp = tempfile.NamedTemporaryFile(mode="w+t", suffix=".html", delete=False)
        temp.write(output)
        temp.seek(0)
        webbrowser.open(temp.name)
    
    else:
        with open(html_outputfile, 'w+') as f:
            f.write(output)
        webbrowser.open(html_outputfile)


def open_jupyter(filepath, test):
    import subprocess
    import os
    import sys    

    process = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__),  ".." , "util", "open_jupyter.py"), filepath], stdout=subprocess.PIPE)

    if test:
        return

    try:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print (output.strip())
        rc = process.poll()
        return rc
    except KeyboardInterrupt:
        sys.exit(0)


def open_editor(notebook_filename, editor):
    import sys, tempfile, os
    from subprocess import call
    EDITOR = os.environ.get('EDITOR', editor)

    call([EDITOR, notebook_filename])