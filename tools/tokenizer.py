import os
import re
import sys
import yaml
import pandas
import numpy


def tokeize_column(df, column_name):
	# lowercase the column
	df[column_name] = df[column_name].str.lower()
	# get unique values
	unique_values = df[column_name].unique()
	tokenized_column = df
	for i in range(len(unique_values)):
		tokenized_column[column_name] = tokenized_column[column_name].replace(unique_values[i], i)
	return tokenized_column


def main():
	if len(sys.argv) != 4:
		sys.stderr.write("Arguments error. Usage:\n")
		sys.stderr.write("\tpython prepare.py data-file\n")
		sys.exit(1)
	params = yaml.safe_load(open("params.yaml"))
	input_path = sys.argv[1]
	output_path = sys.argv[2]
	stage_name = sys.argv[3]

	column_to_tokenize = params[stage_name]["column_to_tokenize"]
	dframe = pandas.read_csv(input_path)
	df_tokenized = tokeize_column(dframe, column_to_tokenize)
	output_file_path = os.path.join(output_path, os.path.basename(input_path))
	os.makedirs(output_path, exist_ok=True)
	df_tokenized.to_csv(output_file_path, index=False)


if __name__ == "__main__":
	main()