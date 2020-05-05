## tools
very useful tools in dadily(incuding kitti)

datasetconvert.py can convert kittidataset tracking to kittidataset detection format

## usage

on windows,you need to change this code row 22;
on linux,you need to annotating code row 22.

first you need to donwload kitti tracking dataset,and change the filename 'object_tracking' to 'object'
Then you can

```
$python datasetconvert.py 
```
Then you can have what you want in file 'object_tracking'.

## news
2020.5.5.
now the code can fix the /training/label_2 file which do not mark,i mark it dontcare,and move all the file dontcare to the last,fix the calibfile bug.

2020.4
can convert trackingdataset normally,calibfile may be some problems