import pandas as pd


def read_and_display_csv(file_path):
    """
    Reads a CSV file and prints its columns and rows.

    Parameters:
    file_path (str): The path to the CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Loop through all rows and print
    print("\nRows:")
    transcriptions = []
    for _, row in df.iterrows():
        transcriptions.append(row["transcription"])
    return transcriptions