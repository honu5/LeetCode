class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        f=0
        s=0
        players.sort()
        trainers.sort()
       
        n=max(len(players),len(trainers))
        cnt=0
        if len(players)<=len(trainers):
            while n:
                if players[f]<=trainers[s]:
                    f+=1
                    s+=1
                    
                
                    cnt+=1
                
                else: 
                    s+=1
                n-=1
        else:
            n=min(len(players),len(trainers))
            while n:
                if players[f]<=trainers[s]:
                    f+=1
                    s+=1
                    
                
                    cnt+=1
                    n-=1
                
                else: 
                    s+=1
                

            
                    
        return cnt

            