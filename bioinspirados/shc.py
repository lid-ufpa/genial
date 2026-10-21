import random
from typing import Callable, Any, Tuple, List, Optional, Dict

State = Any

class StochasticHillClimbing:
    """
    A simple Stochastic Hill Climbing optimizer.
    """
    def __init__(
        self,
        objective_fn: Callable[[State], float],
        neighbor_fn: Callable[[State], State],
        random_state_fn: Callable[[], State],
        maximize: bool = True,
        max_iters: int = 10_000,
        restarts: int = 1,
        no_improve_limit: int = 500,
        rng: Optional[random.Random] = None,
    ):
        self.objective_fn = objective_fn
        self.neighbor_fn = neighbor_fn
        self.random_state_fn = random_state_fn
        self.maximize = maximize
        self.max_iters = max_iters
        self.restarts = max(1, restarts)
        self.no_improve_limit = no_improve_limit
        self.rng = rng or random.Random()
        
        self.best_state_: Optional[State] = None
        self.best_score_: Optional[float] = None
        self.history_: List[float] = []
    
    def _better(self, a: float, b: float) -> bool:
        return a > b if self.maximize else a < b
    
    def run(self, initial_state: Optional[State] = None) -> Tuple[State, float]:
        global_best_state = None
        global_best_score = None
        
        for _ in range(self.restarts):
            state = initial_state if initial_state is not None else self.random_state_fn()
            score = self.objective_fn(state)
            best_local_state, best_local_score = state, score
            
            no_improve_steps = 0
            for step in range(self.max_iters):
                neighbor = self.neighbor_fn(state)
                neighbor_score = self.objective_fn(neighbor)
                
                if self._better(neighbor_score, score):
                    state, score = neighbor, neighbor_score
                    no_improve_steps = 0
                    if self._better(score, best_local_score):
                        best_local_state, best_local_score = state, score
                else:
                    no_improve_steps += 1
                
                self.history_.append(best_local_score)
                
                if no_improve_steps >= self.no_improve_limit:
                    break
            
            if (global_best_score is None) or self._better(best_local_score, global_best_score):
                global_best_state, global_best_score = best_local_state, best_local_score
        
        self.best_state_ = global_best_state
        self.best_score_ = global_best_score
        return global_best_state, global_best_score
    
def nqueens_random_state(N: int, rng: Optional[random.Random] = None) -> List[int]:
    rng = rng or random.Random()
    return [rng.randrange(N) for _ in range(N)]

def nqueens_num_conflicts(state: List[int]) -> int:
    N = len(state)
    conflicts = 0
    # count attacking pairs
    for r1 in range(N):
        c1 = state[r1]
        for r2 in range(r1 + 1, N):
            c2 = state[r2]
            same_col = (c1 == c2)
            same_diag = (abs(c1 - c2) == abs(r1 - r2))
            if same_col or same_diag:
                conflicts += 1
    return conflicts

def nqueens_objective(state: List[int]) -> float:
    # higher is better -> use negative conflicts; best is 0.0
    return -float(nqueens_num_conflicts(state))

def nqueens_neighbor(state: List[int], rng: Optional[random.Random] = None) -> List[int]:
    rng = rng or random.Random()
    N = len(state)
    # choose a random row and move its queen to a different random column
    row = rng.randrange(N)
    new_col = rng.randrange(N - 1)
    if new_col >= state[row]:
        new_col += 1  # ensure different from current column
    neighbor = list(state)
    neighbor[row] = new_col
    return neighbor

class NQueensProblem:
    def __init__(self, N: int = 8, seed: Optional[int] = None):
        self.N = N
        self.rng = random.Random(seed)
    
    def random_state(self) -> List[int]:
        return nqueens_random_state(self.N, self.rng)
    
    def neighbor(self, state: List[int]) -> List[int]:
        return nqueens_neighbor(state, self.rng)
    
    def objective(self, state: List[int]) -> float:
        return nqueens_objective(state)
    
    def pretty_board(self, state: List[int]) -> str:
        N = self.N
        lines = []
        for r in range(N):
            line = ["·"] * N
            line[state[r]] = "Q"
            lines.append(" ".join(line))
        return "\n".join(lines)