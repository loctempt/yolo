import xml.etree.ElementTree as ET
from os import getcwd
import os

# sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
# sets=[('2007', 'train')]

classes = ['car', 'traffic_sign', 'truck', 'pedestrian_crossing', 'bicycle', 'road_mark', 'bus', 'pedestrian', 'motorcycle']


def convert_annotation(image_id, list_file):
    in_file = open('d:/convert/valid_dataset/Annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

# for year, image_set in sets:
image_ids = [img_name[:-4] for img_name in os.listdir('d:/convert/valid_dataset/BMPImages')]
# print(image_ids)
list_file = open('2019_self_data_set.txt', 'w')
for image_id in image_ids:
    list_file.write('d:/convert/valid_dataset/BMPImages/%s.bmp'%(image_id))
    convert_annotation(image_id, list_file)
    list_file.write('\n')
list_file.close()

