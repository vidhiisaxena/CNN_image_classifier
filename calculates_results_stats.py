#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-clan_imagesify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:Vidhi Saxena
# DATE CREATED: 15/11/2024                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the clan_imagesifier's model 
#          architecture to clan_imagesify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for clan_imagesifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          clan_imagesifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & clan_imagesifier labels
#            n_correct_dogs - number of correctly clan_imagesified dog images
#            n_correct_notdogs - number of correctly clan_imagesified NON-dog images
#            n_correct_breed - number of correctly clan_imagesified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly clan_imagesified dogs
#            pct_correct_breed - percentage of correctly clan_imagesified dog breeds
#            pct_correct_notdogs - percentage of correctly clan_imagesified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using clan_imagesifier's model 
    architecture to clan_imagesifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for clan_imagesifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = clan_imagesifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            clan_imagesifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Clan_imagesifier clan_imagesifies image 
                            'as-a' dog and 0 = Clan_imagesifier clan_imagesifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the clan_images for details
                     on how to calculate the counts and statistics.
    """     
    
    results_stats_dic={
        'n_dogs_img':0,
        'n_match':0,
        'n_correct_dogs':0,
        'n_correct_notdogs':0,
        'n_correct_breed': 0,
        'n_images':len(results_dic),
        'n_notdogs_img':0
    }
    
    
    for key in results_dic:
        if (results_dic[key][2]==1):
                results_stats_dic['n_match']+=1
        if (results_dic[key][2]==1) and (results_dic[key][3]==1):
                results_stats_dic['n_correct_breed']+=1
        if results_dic[key][3]==1:#Pet is a dog
                results_stats_dic['n_dogs_img']+=1
                if results_dic[key][4]==1:
                        results_stats_dic['n_correct_dogs']+=1
        else:#Pet is not a dog
                results_stats_dic['n_notdogs_img']+=1
                if results_dic[key][4]==1:
                        results_stats_dic['n_correct_notdogs']+=1
    if results_stats_dic['n_images']>0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match']/ results_stats_dic["n_images"]) * 100 
    else:
        results_stats_dic['pct_match']=0.0
    
    if results_stats_dic['n_dogs_img']>0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs']/results_stats_dic['n_dogs_img'])*100
        results_stats_dic['pct_correct_breed']=  (results_stats_dic['n_correct_breed']/results_stats_dic['n_dogs_img'])*100
    else:
        results_stats_dic['pct_correct_dogs']=0.0
        results_stats_dic['pct_correct_breed']=0.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /results_stats_dic['n_notdogs_img'])*100
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    return results_stats_dic
