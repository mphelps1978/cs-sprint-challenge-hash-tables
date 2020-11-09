def has_negatives(a):

   ht = {}
   result = []

   # loop through the list, and set a desired value of the current number's negative value (by multiplying by -1)

   for number in a:
       desired = number * (-1)

   ## if the desired number is less than the current number (the negative opposite) - Then it has a negative - Add it to the results
   ## otherwise, we're adding the desired number
       if desired in ht:
           if number > desired:
               result.append(number)
           else:
               result.append(desired)
   ## if it's not in the table, then we need to add it, by setting a key of the number, and a value of it's opposite
       else:
           ht[number] = desired
   return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
