import pandas as pd
import sqlite3
import os

def load_data_to_db(df, db_path, error_log_path):
	# Connect to the SQLite database 'kapustin.db'
	conn = sqlite3.connect(db_path)

	if not os.path.exists(os.path.dirname(error_log_path)):
		os.makedirs(os.path.dirname(error_log_path))

	# Try to load the dataframe into the database
	try:
		df.to_sql('works', conn, if_exists='replace', index=False)
		with open(error_log_path, 'a') as log_file:
			log_file.write(f"Successfully loaded {len(df)} items.\n")
	except Exception as e:
		with open(error_log_path, 'a') as log_file:
			log_file.write(f"Error loading data: {str(e)}\n")

	# Close the connection
	conn.close()

def main():
	# Read the CSV file into a pandas DataFrame
	df = pd.read_csv('../data/kapustin_works.csv')

	# Convert the 'RecordingExists' column to a boolean
	df['recording_exists'] = df['recording_exists'].astype(bool)

	# Calculate the NumberOfSections based on the ListOfSectionNames
	df['num_sections'] = df['section_names'].str.split(',').apply(lambda x: len(x) if isinstance(x, list) else 1)

	# Load the data to the SQLite database
	load_data_to_db(df, 'kapustin.db', './error_log.txt')

if __name__ == "__main__":
	main()