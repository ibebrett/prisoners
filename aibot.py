import logging
import os

has_openai = False

try:
   from openai import OpenAI
   has_openai = True
except ImportError:
    pass

from participant import Move, Prisoner

prompt = '''
You are playing a game of iterated prisoners dillema. Your moves are COOPERATE and DEFECT.
It is a tournament where you will end up playing a variety of opponents and your points
will be added up. In this conversation we will be only playing against one opponent,
but your points will be totalled accross all rounds. The payouts are

1. Both cooperate: 3 points for all
2. Both defect: 1 point for all
3. One defects, one cooperates. The defector gets 5 and the cooperator gets 1.

I'll tell you the moves the opponent makes and you tell me the next move by writing 
the word COOPERATE or DEFECT only. Only respond with one of those words at a time.

so far your moves have been: {your_moves}
and your opponents have been: {opponents_moves}

Please respond with the move you will make next in the first line.
Then in the 2nd line explain why you made that move.
'''


logger = logging.getLogger(__name__)

class AIBot(Prisoner):
    def __init__(self):
        self.my_moves = []
        self.their_moves = []
        self.client = None
        if has_openai:
            self.client = OpenAI(
                api_key=os.environ.get('OPENAI_API_KEY')
            )


    @classmethod
    def get_name(self) -> str:
        return "AIBot"
    
    def play(self) -> Move:
        if self.client is None:
            return Move.COOPERATE

        curr_prompt = prompt.format(your_moves=[s.value for s in self.my_moves],opponents_moves=[s.value for s in self.their_moves])
        
        logger.warning("Sending to chat gpt")
        logger.warning(curr_prompt)

        response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": "you are an agent playing iterated prisoners dillema"},
                    {"role": "user", "content": curr_prompt}
                ]
        )
        message = response.choices[0].message.content
        message = message.strip()
        lines = message.split('\n')
        extra = ''
        if len(lines) > 0:
            message = lines[0]
        if len(lines) > 1:
            extra = "\n".join(lines[1:])

        move = None
        if message == 'COOPERATE':
            move = Move.COOPERATE
        elif message == 'DEFECT':
            move = Move.DEFECT

        logger.warning('Response from openai')
        logger.warning(message)
        logger.warning('Explanation')
        logger.warning(extra)

        if move is None:
            logger.warn(f'OPEN API didnt return a real response: {message}')
            move = Move.COOPERATE

        self.my_moves.append(move)
        return move

    def result(self, your_mdove: Move, their_move: Move, payout: int, their_payout: int) -> None:
        self.their_moves.append(their_move)

