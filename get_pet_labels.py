#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Vidhi Saxena
# DATE CREATED: 15/11/2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    from os import listdir
    #list of image directory
    listdr=listdir(image_dir)
    #define results_dics dictionary
    results_dic=dict()
    #Traversing through the list of items in listdr
    for i in range(0,len(listdr)):
      if listdr[i][0] != ".":
        pet_label=str()
        pet_img= listdr[i]
        pet_img=pet_img.replace("_"," ").lower()
        pet_label= "".join(char for char in pet_img if char.isalpha() or char.isspace()).replace("jpg","")
        pet_label=pet_label[:-1]
        if listdr[i] not in results_dic:
         results_dic[listdr[i]] = [pet_label]
        else:
          print("** Warning: Key=", listdr[i], "already exists in results_dic with value =", results_dic[listdr[i]])

    #Iterating through a dictionary printing all keys & their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
      print("Filename=", key, "   Pet Label=",results_dic[key][0])


    # Replace None with the results_dic dictionary that you created with this
    # function
    return(results_dic)