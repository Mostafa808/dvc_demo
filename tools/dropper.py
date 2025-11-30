import os
import re
import sys
import yaml
import pandas
import numpy

def drop_column(dataframe, column_name):
    return dataframe.drop(column_name, axis=1)

def main():
	if len(sys.argv) != 4:
		sys.stderr.write("Arguments error. Usage:\n")
		sys.stderr.write("\tpython prepare.py data-file\n")
		sys.exit(1)
	params = yaml.safe_load(open("params.yaml"))
	input_path = sys.argv[1]
	output_path = sys.argv[2]
	stage_name = sys.argv[3]

	column_to_drop = params[stage_name]["column_to_drop"]
	dframe = pandas.read_csv(input_path)
	df_dropped = drop_column(dframe, column_to_drop)
	output_file_path = os.path.join(output_path, os.path.basename(input_path))
	os.makedirs(output_path, exist_ok=True)
	df_dropped.to_csv(output_file_path, index=False)

if __name__ == "__main__":
	main()