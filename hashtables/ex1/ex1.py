def get_indices_of_item_weights(weights, length, limit):

   ht = {}
   # as we cycle through the weights, we want to calculate the desired weight and then check it against the hashtable
   for i, w in enumerate(weights):
       desired_weight = limit - w

       if desired_weight in ht:
           return(i, ht[desired_weight])
       # and if it's not there, we need to add it
       ht[w] = i

   return None
