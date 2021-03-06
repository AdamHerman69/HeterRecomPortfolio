#!/usr/bin/python3

import pandas as pd

class ResultOfRecommendation:

   # itemIDs:list<int>, ratings:list<float>
   def __init__(self, itemIDs, ratings):
      if type(itemIDs) is not list :
         raise ValueError("Argument itemIDs is not type list.")
      if type(ratings) is not list :
         raise ValueError("Argument ratings is not type list.")

      for itemIDI in itemIDs:
         if type(itemIDI) is not int:
            raise ValueError("Argument itemIDs contains an item of the wrong type (not str).")
      for ratingI in ratings:
         if type(ratingI) is not float:
            raise ValueError("Argument ratings contains an item of the wrong type (not float).")

      if len(itemIDs) != len(list(dict.fromkeys(itemIDs))):
         raise ValueError("Argument itemIDs contains duplicate itemIDs values.")
      if len(itemIDs) != len(ratings):
         raise ValueError("Arguments itemIDs (list) and ratings (list) are not the same length.")

      self._itemIDs = itemIDs;
      self._ratings = ratings;


   def exportAsSeries(self):
      return pd.Series(self._ratings, self._itemIDs, name="rating")



