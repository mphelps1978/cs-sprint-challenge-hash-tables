def intersection(arrays):

   ht = {}
   checking = len(arrays)
   result = []

   #Cycle through each array, and check to see if each value is in the HT.
   ## If it is, then add 1 to the value (We've seen it more than once)
   ## If not, needs to be added..
   for x in arrays:
       for y in x:
           if y not in ht:
               ht[y] = 1

   # After we've cycled through, we look at the HT. If the number if occurances for a value is the same as the
   # number of arrays, we've found a common index - Add it to the list.
           else:
               new_count = ht[y] + 1
               ht[y] = new_count
               if new_count == checking:
                   result.append(y)

   return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
