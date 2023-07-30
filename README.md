# Map_reduce-Bigdata
This repository contains a Python implementation of a Map-Reduce code to count the number of deaths caused by COVID-19 in each African country.

Prerequisites:

Before running the code, make sure you have Hadoop installed on your machine. You can choose one of the following options:

    1-LHM for Minimal VirtualBox: You can follow the instructions provided in this link for a minimal installation of Hadoop on a VirtualBox: LHM for Minimal VirtualBox. This option is recommended for a simple setup.

    2-CLOUDERA: Alternatively, you can use CLOUDERA for Hadoop installation. For more details, refer to the official Cloudera website.

Hadoop Documentation:

For further information about Hadoop and HDFS/DFS, you can visit the official Apache Hadoop documentation: Hadoop Commands Manual.

Running the Code:

Once you have Hadoop installed, follow the steps below to execute the Map-Reduce code:

    1-Connect via SSH: Launch the command line and connect to your SSH client.

    2-Copy Files to HDFS: Use another terminal to copy the mapper, reducer, and the deaths Africa files to the HDFS.

    3-Run the Command: After the files are successfully copied, run the following command to execute the Map-Reduce job:

    $ hadoop jar /opt/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-
    3.3.0.jar \
    
    -file ./mapper.py -mapper ./mapper.py \
    -file ./reducer.py -reducer ./reducer.py \
    -input /user/USERNAME/africa_covid19_daily_deaths_national.txt \
    -output /user/USERNAME/pyDeathsCountOut

Note:
Ensure you have access to the necessary datasets and permissions before running the code. Also, keep in mind that this code is specifically designed to count COVID-19 deaths in African countries using Hadoop's Map-Reduce paradigm.
