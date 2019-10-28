# LeetCode: Problem 412
# Jonathan Kosasih

#Write a program that outputs the string representation of numbers from 1 to n.
#
#But for multiples of three it should output “Fizz” instead of the number and
#for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
#Example:
#n = 15,
#
#Return:
#[
#    "1",
#    "2",
#    "Fizz",
#    "4",
#    "Buzz",
#    "Fizz",
#    "7",
#    "8",
#    "Fizz",
#    "Buzz",
#    "11",
#    "Fizz",
#    "13",
#    "14",
#    "FizzBuzz"
#]
#------------------------------------------------------------------
class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        index = 1
        while(index <= n):
            if(index % 3 == 0 and index % 5 == 0):
                ans.append("FizzBuzz")
            elif(index % 3 == 0):
                ans.append("Fizz")
            elif(index % 5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(index))
            index += 1
        return ans
    
    def fizzBuzzAlt(self, n: int):
        ans = []
        index = 1
        while(index <= n):
            div3 = (index % 3 == 0)
            div5 = (index % 5 == 0)
            string = ""
            if(div3):
                string += "Fizz"
            if(div5):
                string += "Buzz"
            if(not string):
                string = str(index)
            ans.append(string)
            index += 1
        return ans
    
    def fizzBuzzHash(self, n:int):
        # ans list
        ans = []
        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        for num in range(1,n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str = str(num)
            # Append the current answer str to the ans list
            ans.append(num_ans_str)  
        return ans
    
sol = Solution()
n = 15
print(sol.fizzBuzz(n))
n = 15
print(sol.fizzBuzzAlt(n))
n = 15
print(sol.fizzBuzzHash(n))