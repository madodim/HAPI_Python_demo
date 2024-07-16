# Basic demo of hapiclient.
# See http://hapi-server.org/servers/ for a list of other HAPI servers and datasets.

# Import the required libraries
from hapiclient import hapi
import pandas as pd
import matplotlib.pyplot as plt
import time


# Define functions for each section of the process
def define_server_and_dataset():
    """
    Define the HAPI server URL, dataset, and parameters.
    """
    server = 'https://cdaweb.gsfc.nasa.gov/hapi'
    dataset = 'OMNI2_H0_MRG1HR'  # OMNI2 dataset
    parameters = 'DST1800'  # Correct DST index parameter
    return server, dataset, parameters


def define_time_range():
    """
    Define the start and stop times for the data request.
    """
    start = '2015-01-01T00:00:00Z'  # Example start time
    stop = '2020-01-01T00:00:00Z'  # Example stop time
    return start, stop


def request_data(server, dataset, parameters, start, stop):
    """
    Request and download the data from the HAPI server.
    """
    data, meta = hapi(server, dataset, parameters, start, stop)
    return data, meta


def save_data_to_file(data):
    """
    Save the downloaded data to a CSV file.
    """
    # Convert the data to a DataFrame (if the data format is compatible)
    df = pd.DataFrame(data)
    # Save the DataFrame to a CSV file
    print(df.info())
    #minimum value
    if 'DST1800' in df.columns:
        print("Minimum value of the DST index [nT]:", df['DST1800'].min())
    else:
        print("DST1800 column not found in the DataFrame.")
    df.to_csv('omni2_dst_data.csv', index=False)
    print("Data downloaded and saved to omni2_dst_data.csv")
    return df


def plot_data(df):
    """
    Plot the data using Matplotlib.
    """
    if 'Time' in df.columns and 'DST1800' in df.columns:
        # Decode the byte objects to strings and convert to datetime
        df['Time'] = df['Time'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
        df['Time'] = pd.to_datetime(df['Time'])
        plt.figure(figsize=(10, 6))
        plt.ion()
        plt.plot(df['Time'], df['DST1800'], label='DST Index')
        plt.xlabel('Time [Years]')
        plt.ylabel('DST Index [nT]')
        plt.title('Time Series of DST Index')
        plt.legend()
        plt.grid(True)
        plt.show()
        plt.pause(3)
        plt.savefig('dst_plot.png')
    else:
        print("DataFrame does not contain required columns for plotting.")


# Main function to coordinate the data download process
def main():
    start_time = time.time()  # Record the start time
    print("\nStarting the main process...")

    # Define server and dataset
    server, dataset, parameters = define_server_and_dataset()

    # Define time range
    start, stop = define_time_range()

    # Request and download data
    data, meta = request_data(server, dataset, parameters, start, stop)

    # Save the data to a file
    df = save_data_to_file(data)

    # Plot the data
    plot_data(df)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  # Print the elapsed time
    exit()

# Run the main function
if __name__ == "__main__":
    main()
