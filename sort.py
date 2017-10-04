import yaml
import sys

fname = sys.argv[1]

stream = open(fname, 'r')
data = yaml.load(stream)

with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
