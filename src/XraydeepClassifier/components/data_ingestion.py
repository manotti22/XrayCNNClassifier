import os
import urllib.request as request
from XraydeepClassifier.entity import DataIngestionConfig
from XraydeepClassifier import logger
from XraydeepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path
import nibabel as nib
import matplotlib.pyplot as plt
import shutil


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def input_data(self):
        logger.info("Trying to input data path...")
        data_path = Path(self.config.local_data_file)

        if not os.path.exists(self.config.local_data_file):
            logger.info("data input started...")
        with open(os.path.join(data_path, "data.nii"), "r") as f:

            data = f.read()

        #This opens the file data.nii in the directory path/to/your/data relative to the current working directory, reads its contents, and stores them in the variable data.

        logger.info(f"{data} is pushed in: \n{data_path}")
    
        logger.info(f"data already exists of size: {get_size(Path(self.config.local_data_file))}")        



    def nii_to_png(nii_file, png_file):
        def __init__(self, config: DataIngestionConfig):
            self.config = config
              # Convert all nii to png
            data_path = Path(self.config.local_data_file)
            nii_file= data_path
            png_file=""

        # Load NIfTI file
        img = nib.load(nii_file)[0]
        # Get image data
        img_data = img.get_fdata()
        # Plot the image data
        plt.imshow(img_data[:, :, img_data.shape[-1]//2], cmap='gray')
        plt.axis('off')
        # Save the plot as a PNG file
        plt.savefig(png_file, bbox_inches='tight', pad_inches=0, dpi=100)
        plt.close()

    def convert_all_niis(self):
    # Get list of all NIfTI files in the directory
        logger.info("Trying to convert nii data to png...")

        niis = [f for f in os.listdir(self.config.local_data_file) if f.endswith('.nii')]
    # Loop through all NIfTI files and convert them to PNG
        for nii in niis:

            nii_path = os.path.join(self.config.local_data_file, nii)
            png_path = os.path.join(self.config.local_data_file, nii.replace('.nii', '.png'))
        logger.info("Png data converting succesfully...")


    def remove_niis(self):

    # Get list of all NIfTI files in the directory
        logger.info("Removing nii data files...")
        niis = [f for f in os.listdir(self.config.local_data_file) if f.endswith('.nii')]
    # Loop through all NIfTI files and remove them
        for nii in niis:

            nii_path = os.path.join(self.config.local_data_file, nii)
            os.remove(nii_path)
            logger.info("nii data files removed succesfully...")

    def divide_pngs(self):

    # Define the names of the 6 files
        logger.info("Dividing Data to 6 Categorical Folder...")
        file_names = ['-Flair.png', '-LesionSeg-Flair.png', '-LesionSeg-T1.png', '-LesionSeg-T2.png', '-T1.png', '-T2.png']
    # Loop through all the files in the directory
        for file in os.listdir(self.config.local_data_file):

            if file.endswith('.png'):

            # Get the name of the file without the numbers at the beginning
                name_without_numbers = file
                while name_without_numbers[0].isdigit():
                    name_without_numbers = name_without_numbers[1:]
            # Check if the name without numbers is in the list of the 6 files
            if name_without_numbers in file_names:
                file_path = os.path.join(self.config.local_data_file, file)
                folder_path = os.path.join(self.config.local_data_file, name_without_numbers.split('.')[0])
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                logger.info("Data is succesfully in 6 Folder divided...")

    def create_test_data(self):
        """
        separte 30% of data into test data
        """
        pass