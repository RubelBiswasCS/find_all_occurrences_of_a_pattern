def find_count(string,target,count=0,n=0):
    if string[n:n+len(target)] == target:
        count+=1
    if len(string) == len(target):
        return count
    else:
        return find_count(string[n+1:],target,count)
   
string = 'adadattaetadadadafa'
target = 'dada'

print(f'Pattern "{target}" appears in text "{string}" {find_count(string,target)} times')

'''
    Here find_count function which take 4 arguments. while last 2 have a default parameters initialized
    with 0, and string is the input string aganist which the target pattern will be searched.Its 
    basically a recusive function.

    in first statement of the function it will take same number of charecter from the nth index of thd
    string and will match it with the target pattern. if it is equal the count will be increase by 1.

    then in the next if/else clouse, the length of the string will be checked with the substing/target
    if the substring is equal to the main string its means we are end of the string, so it will return 
    the count on the other hand in the string is greater than the substing, function will return 
    itself/find_count with increased value of n means main string with on less character at the begining 
    and updated value of count.
    
     find_count (string to be searched, pattern, count initially 0, index n=0){
        if string[index to index+length of pattern] is equal to pattern{
            increase count by 1
        }
        if lenght of string is equal to target{
            return count, end of recursion
        }
        else lengtg of string is greater than target's lenght{
            make recursive call with string without the very first charcter and updated count.
        }
    }
    
'''


