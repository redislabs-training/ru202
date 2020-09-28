'''
Redis Streams utilities
'''

# Maximal value of sequence part in a message ID
__MAX_SEQ__ = 2**64 - 1

def incr_id(_id):
    ''' Increment a Stream message ID by one '''
    t, s = map(int, str(_id).split('-'))
    if s == __MAX_SEQ__:  # Handle overflow
        t += 1
        s = 1
    else:
        s += 1
    return f'{t}-{s}'

def decr_id(_id):
    ''' Decrement a Stream message ID by one '''
    t, s = map(int, str(_id).split('-'))
    if s == 0:  # Handle underflow
        t -= 1
        s = __MAX_SEQ__
    else:
        s -= 1
    return f'{t}-{s}'
