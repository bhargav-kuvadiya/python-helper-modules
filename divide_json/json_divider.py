import json
import sys

def divide(json_file, chunk_size=500, output_folder='output_folder', custom_names):
  with open(json_file,'r') as infile:
    o = json.load(infile)
    chunkSize = chunk_size
    for i in xrange(0, len(o), chunkSize):
      name = custom_names[i] or json_file + '_' + str(i//chunkSize)
      with open(output_folder + '/' + name + '.json', 'w') as outfile:
        json.dump(o[i:i+chunkSize], outfile)