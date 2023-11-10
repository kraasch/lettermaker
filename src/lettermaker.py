#!/usr/bin/python3

import subprocess
import argparse
import os
import pathlib
import toml
from datetime import datetime
import shutil

# parse arguments.
parser = argparse.ArgumentParser(prog='lettermaker')
parser.add_argument('-t', '--toml',     type=str, help='Compile a letter from TOML to PDF.')
parser.add_argument('-d', '--defaults', type=str, help='Path to default files.')
parser.add_argument('-o', '--output',   type=str, help='Output file name.')
parser.add_argument('-T', '--template', type=str, help='Create TOML template.')
args = parser.parse_args()

# get path to project.
bin_path = pathlib.Path(__file__)
# if needed follow symlinks.
while os.path.islink(bin_path):
    bin_path=os.readlink(bin_path) # follow the link.
    bin_path=pathlib.Path(bin_path) # convert str to Path.
project_root=str(bin_path.parent.parent)

# create toml templte.
if args.template:
    shutil.copyfile(project_root + '/example/empty.toml', args.template + '.toml')
    exit()

# create output folder.
output_path='./output/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

# returns today's date as string.
def today():
    return datetime.today().strftime('%Y-%m-%d')

# read in toml file as dictionary.
def toml_to_dict(file_name):
    with open(file_name, 'r') as f:
        toml_string = f.read()
        parsed_toml = toml.loads(toml_string)
    return parsed_toml

# read toml file.
letter_toml = toml_to_dict(args.toml)
template_type = letter_toml['meta']['template']
fields = letter_toml['fields']

# open the letter template.
template_file= project_root + '/templates/' + template_type + '.tex'
letter_template=''
with open(template_file) as f:
    letter_template=f.read()

# open default content.
if not args.defaults:
    defaults_path = project_root + '/defaults/'
else:
    defaults_path = args.defaults
    if not defaults_path.endswith('/'):
        defaults_path = defaults_path + '/'
defaults_file = defaults_path + template_type + '.toml'
defaults_toml = toml_to_dict(defaults_file)
default_fields = defaults_toml['fields']

# replaces one variable in latex template text.
def replace_latex_var(latex, key, content):
    regex=r'\VAR{' + key.upper() + '}'
    return latex.replace(regex, content)

# compile the letter.
temp_file='./output/letter.tex'
if args.toml:
    with open(temp_file, 'w') as f:
        latex=letter_template
        for key, content in fields.items():
            if content == '':
                if key == 'date':
                    content = today()
                else:
                    content = default_fields[key]
            latex = replace_latex_var(latex, key, content)
        f.write(latex)
    rc = subprocess.call(['pdflatex', '-halt-on-error', '-output-directory', output_path, temp_file])
    if args.output:
        shutil.move(output_path + '/letter.pdf', args.output + '.pdf')
        shutil.rmtree(output_path)
    exit()

