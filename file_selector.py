#!/usr/bin/python3

import os
import jfiles
import jfolders


def change_to_file_directory():
  """Changes the current working directory to the directory of the executing script."""
  abspath = os.path.abspath(__file__)
  dname = os.path.dirname(abspath)
  os.chdir(dname)



def main():
    # Call the function to change directory
    change_to_file_directory()
    print("File Selector: Choose your file!")
    while(True):
        source_folder = jfiles.get_value_from_file("file_selector.conf", "source-folder", default=None)
        entries = jfolders.get_folder_entries(source_folder)
        entries.sort()
        for i in range(len(entries)):
            print("[" + str(i) + "]\t" + entries[i].replace(source_folder+"/", ""))
        number = input("Number (q for quit): ")
        if number == "q":
            return
        index = int(number)
        if index < 0 or index >= len(entries):
            print("!!!!Error: Number out of range!!!!")
            continue
        print("Choosing " + entries[index] + " ...")
        jfiles.copy_file(entries[index], jfiles.get_value_from_file("file_selector.conf", "destination-file", default="output.png"))
        print("--------------------------------------------------------------")


if __name__ == "__main__":
    main()
