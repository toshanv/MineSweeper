from .advanced_agent import start_outside
from ..board_utils.board import Board
from ..core.agent import Agent


def start(board: Board, agent: Agent, use_stepping: bool = False, lock_boolean=None):
    start_outside(board, agent, use_stepping, lock_boolean,
                  hyper_advanced=True, bonus1=False, bonus2=False)
