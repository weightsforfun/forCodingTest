class Solution:               ## int해주면 0이 없어지네
    def reverse(self, x: int) -> int:
        string=list(str(x))
        is_it_negative=0

        while(True):
            if(len(string)>=1):
                if(string[-1]=='0'):
                    string.pop(-1)
                else:
                    break
            else:
                break
        if(len(string)==0):
            return 0
        
        else:
            if(string[0]=='-'):
                is_it_negative=1

            if(is_it_negative):
                string.pop(0)
                string=string[::-1]
                answer= int('-'+''.join(string))
                if(answer>((2**31)-1) or answer<-1*(2**31)):
                    return 0
                else:
                    return answer
            else:
                string=string[::-1]
                answer= int(''.join(string))
                if(answer>((2**31)-1) or answer<-1*(2**31)):
                    return 0
                else:
                    return answer

