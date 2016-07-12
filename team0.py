####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team JamesGary'
strategy_name = 'Odd/Even'
strategy_description = 'Odd=c, Even=b'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
  
    Returns 'c' or 'b' for collude or betray.
    '''

    
    if len(my_history) % 2 == 0:
        return 'b'
    else:
        return 'c' 
          