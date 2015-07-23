from collections import Counter
with open('out.txt','r') as q:
	strings=q.read().splitlines()




def substrings(s, minlength=30):
    """Finds all possible unique substrings of s, given a minimum length.

    >>> substrings("12345")
    {'1234', '234', '345', '12345', '123', '2345'}
    >>> substrings("123123")
    {'2312', '123123', '12312', '123', '23123', '1231', '231', '3123', '312'}
    >>> substrings("aaaaa")
    {'aaaaa', 'aaaa', 'aaa'}
    """
    maxsize = current = len(s)
    result = []
    while current >= minlength:
        result.extend([s[start:start+current] 
                       for start in range(maxsize-current+1)])
                                  # range(5) is [0,1,2,3,4]
        current -= 1
    return set(result) # set() removes duplicates

def all_substrings(strings, minlength=30):
    """Returns the union of all the sets of substrings of a list of strings.

    >>> all_substrings(["abcd", "1234"])
    {'123', 'abc', 'abcd', '1234', 'bcd', '234'}
    >>> all_substrings(["abcd", "bcde"])
    {'abc', 'bcd', 'cde', 'abcd', 'bcde'}
    """
    result = set()
    for s in strings:
        result |= substrings(s, minlength)
        # "|=" is the set union operator
    return result




def count(strings, minlength=30):
    """Counts the occurrence of each substring within the provided list of strings,
    given a minimum length for each substring.

    >>> count(["abcd", "bcde"])
    Counter({'bcd': 2, 'bcde': 1, 'abc': 1, 'abcd': 1, 'cde': 1})
    """
    substrings = all_substrings(strings, minlength)
    counts = Counter()
    for substring in substrings:       # Check each substring
         for string in strings:        # against each of the original strings
             if substring in string:   # to see whether it is contained there
                 counts[substring] += 1
    return counts

def prune(counts, mincount=2):
    """Returns only the longest substrings whose count is >= mincount.
    First, all the substrings with a count < mincount are eliminated.
    Then, only those that aren't substrings of a longer string are kept.
    >>> prune(Counter({'bla': 5, 'kay': 5, 'oka': 5, 'okay': 5, 'la1': 2, 'bla1': 2}))
    [('okay', 5), ('bla', 5)]
    """
    # Throw out all counts < mincount. Sort result by length of the substrings.
    candidates = sorted(((s,c) for s,c in counts.items() if c >= mincount), 
                        key=lambda l: len(l[0]), reverse=True) # descending sort
    result = []
    seenstrings = set()      # Set of strings already in our result
    # (we could also look directly in the result, but set lookup is faster)
    for item in candidates:
        s = item[0]          # item[0] contains the substring
        # Make sure that s is not already in our result list
        if not any(s in seen for seen in seenstrings): 
            result.append(item)
            seenstrings.add(s)
    return result

counts = count(strings)
listofresult=prune(counts)
listofresult.sort(key=lambda x:x[1],reverse=True)

with open('temp3.txt','r') as q:
	 line=q.read().splitlines()


with open('result.txt','w') as q:
	 for s,c in listofresult[:3]:
		q.write('{}\n'.format(s))
		

with open('result.txt','a') as q:
	 for item in line[:2]:
		q.write('\n\nKeyword_category :- %s' %item)
	
	
