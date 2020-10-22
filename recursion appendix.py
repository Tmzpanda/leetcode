
"""
        bottom-up                                                               top-down
        
                        A. if directed, then alternative - LIS 1d vs Longest Increasing Subarray 2d 
        1. dp          <---------------------------------------------------->  
                                                                                1. dfs memoization
                        B. dfs all solutions - Word Ladder vs Word Break                
        2. backtrack   <---------------------------------------------------->       
        
        
                |                                                                      |       
                |                                                                      |
                |                                                                      |
                |                                                                      |
                | C. traverse + take or not                                            | D. divide conquer - no duplicate sub-problems
                |    Binary Tree Paths                                                 |       
                |                                                                      |
                |                                                                      |
                |                                                                      |
                |                                                                      |
                ↓        E. tree - depth vs height                                     ↓       
        3. traverse     <---------------------------------------------------->   2. divide conquer       
       



     
A.                
                                 LIS 1d - directed
   bottom-up                                             top-down
   dp: set i, update j (according to i)        dfs memoization: update j (according to i)
                                                                1. branches, duplicate sub-problems
                                                                2. reduce to subproblem, return



                                                         A.1    Longest Increasing Subarry 2d - no direction
                                                                dfs memoization:  ------------------------------------> dp? sort - brings direction
                                                                1. branches and duplicate sub ✓
                                                                2. reduce and return ✓
                                                                
                                                         A.2    Insert Star
                                                                dfs
                                                                1. branches and duplicatee sub x
                                                                2. reduce and return ✓
   
   
   
   dp  <------------------------> dfs memoization
 initialization                  break condition
 bottom-up                       top-down
 return                          mem and return
                                                                
                                                                
                                                                
"""
