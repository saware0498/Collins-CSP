import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Jennifer'
strategy_name = 'Beat them at their own game'
strategy_description = 'I am going to beat the opponent at their own game.  If they collude a lot, then I am going to collude more (build trust).  If they betray a lot, then I am going to betray more.  And if the average number of times they collude is between 25% and 75%, then I am going to betray them just a little more than they betray me.'
    
def move(my_history, their_history, my_score, their_score):
    history = their_history
    if(my_history==''):
        return 'c'
    if(len(my_history)>10):
        history = their_history[-10]
    numColludes = 0.0
    avgColludes = 0.0
    for letter in history:
        if(letter=='c'):
            numColludes+=1
    avgColludes = numColludes/len(history)
    print(avgColludes)
    if avgColludes>.75:
        probability=avgColludes+0.02
    elif avgColludes<0.25:
        probability=avgColludes-0.25
    else:
        probability = avgColludes-0.05
    if random.random()<probability:
        return 'c'
    else:
        return 'b'

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             