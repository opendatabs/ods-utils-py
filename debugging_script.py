from textwrap import indent

import ods_utils_py as ods_utils
import json

def main():
    if True: # For testing get_number_of_datasets
        print("Trying to retrieve count of all datasets")
        total_num = ods_utils.get_number_of_datasets()
        print("Total number of datasets:", total_num)
        print()

    if False: # For testing get_dataset_custom_view
        print()
        dataset_id = 100398
        print(f"Trying to retrieve custom views of dataset {dataset_id}")
        custom_view = ods_utils.get_dataset_custom_view(dataset_id=dataset_id)
        print(f"Custom view: {json.dumps(custom_view, indent=4)}")

    if False: # For testing get_dataset_license
        dataset_id = 100397
        print(f"Trying to retrieve the license of dataset {dataset_id}")
        dataset_license = ods_utils.get_dataset_license(dataset_id=dataset_id)
        print(f"License is currently: {dataset_license}")

    if False: # For testing set_dataset_public
        dataset_id = 100397
        print(f"Trying to publish dataset {dataset_id}")
        ods_utils.set_dataset_public(dataset_id=100397, publish=True)
        print("Done.")

    if False: # For testing set_dataset_license
        dataset_id = 100397
        license_id_new = "5sylls5"
        print(f"Trying to retrieve current license id of dataset {dataset_id}")
        license_id_old = ods_utils.get_dataset_license(dataset_id=dataset_id)
        print(f"Found license id {license_id_old}")
        print()
        print(f"Trying to update the license to {license_id_new}")
        ods_utils.set_dataset_license(dataset_id=dataset_id, license_id=license_id_new, publish=True)
        print(f"Successfully changed license id from {license_id_old} to {license_id_new}!")

if __name__ == "__main__":
    main()
