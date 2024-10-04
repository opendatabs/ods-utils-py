import ods_automation_python

def main():
    print("Trying to receive count of all datasets")
    total_num = ods_automation_python.get_number_of_datasets()
    print("Total number of datasets:", total_num)

if __name__ == "__main__":
    main()
