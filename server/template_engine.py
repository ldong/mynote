import pyratemp
import config
import os.path

def render(template, context):
    local_path = os.path.join(config.template_dir, template)
    with open(local_path, 'r') as f:
        raw = f.read()

    tmpl = pyratemp.Template(raw)

    return tmpl(**context).encode('UTF-8')

