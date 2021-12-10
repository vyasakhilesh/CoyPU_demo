import os
import configparser
import rdfizer

config_fname = "../../../config.ini"

# Check if there is already a configurtion file
if not os.path.isfile(config_fname):
    # Create the configuration file as it doesn't exist yet
    cfg_file = open(config_fname, "w")

    # Add content to the file
    Config = configparser.ConfigParser()
    Config.add_section("dataset1")
    Config.set("dataset1", "host", "localhost")
    Config.set("dataset1", "user", "root")
    Config.set("dataset1", "passwd", "my secret password")
    Config.set("dataset1", "db", "write-math")
    Config.add_section("datasets")
    # Config.set(
    #     "datasets",
    #     "datasets_list",
    #     [
    #         "datasets_list1",
    #         "datasets_list2",
    #         "datasets_list3",
    #     ],
    # )
    Config.set("datasets", "number_of_datasets", "1")
    Config.write(cfg_file)
    cfg_file.close()
