----------------------------- MODULE PlanetGatedSchedulerPlusCal -----------------------------

EXTENDS Naturals, Reals, Sequences

CONSTANTS
    K, EMax, CMax, GMax, EpsP, DeltaP,
    KSet, Q, WBar

(***************************************************************************)
(* STATE VARIABLES                                                         *)
(***************************************************************************)

VARIABLES
    E, C, G,       \* planet state
    U,             \* [KSet -> Real] used quota
    Jobs,          \* set of job ids
    JobTribe,      \* [Jobs -> KSet]
    JobCost,       \* [Jobs -> Real]
    JobPriority,   \* [Jobs -> Real]
    JobWeight,     \* [Jobs -> Real]
    JobValid,      \* [Jobs -> BOOLEAN]
    Dispatched     \* set of jobs dispatched in this tick

(***************************************************************************)
(* HELPER DEFINITIONS                                                      *)
(***************************************************************************)

PlanetState == <<E, C, G>>

PlanetError ==
    LET eE == E - EMax
        eC == C - CMax
        eG == G - GMax
    IN <<eE, eC, eG>>

Norm2(v) ==
    LET x == v[1]
        y == v[2]
        z == v[3]
    IN  sqrt(x * x + y * y + z * z)

PlanetOK ==
    Norm2(PlanetError) <= EpsP

PlanetGate ==
    LET n == Norm2(PlanetError)
    IN  Exp(-K * Max(0.0, n))

TribeOK(k) ==
    U[k] <= Q[k]

IndOK(j) ==
    JobValid[j]

EligibleJobs ==
    { j \in Jobs : IndOK(j) }

EligibleJobsPlanet ==
    IF PlanetOK
    THEN EligibleJobs
    ELSE { j \in EligibleJobs : JobWeight[j] >= WBar }

JobScore(j) ==
    JobPriority[j] * JobWeight[j]

(***************************************************************************)
(* PLUSCAL ALGORITHM                                                       *)
(***************************************************************************)

(*
   We model a single scheduler "tick" as one iteration of the main loop.
   Planet dynamics (E,C,G) are left abstract; you can plug in a concrete
   update later if desired.
*)

(*--algorithm PlanetGatedSchedulerAlg
variables
    E, C, G,
    U = [k \in KSet |-> 0.0],
    Jobs,
    JobTribe,
    JobCost,
    JobPriority,
    JobWeight,
    JobValid,
    Dispatched = {};

define
    PlanetError == <<E - EMax, C - CMax, G - GMax>>;
    Norm2(v) == 
        let x == v[1] in
        let y == v[2] in
        let z == v[3] in
        sqrt(x * x + y * y + z * z);
    PlanetOK == Norm2(PlanetError) <= EpsP;
    PlanetGate == 
        let n == Norm2(PlanetError) in
        Exp(-K * Max(0.0, n));
    TribeOK(k) == U[k] <= Q[k];
    IndOK(j) == JobValid[j];
    EligibleJobs == { j \in Jobs : IndOK(j) };
    EligibleJobsPlanet ==
        if PlanetOK then EligibleJobs
        else { j \in EligibleJobs : JobWeight[j] >= WBar };
end define;

begin
  SchedulerLoop:
  while TRUE do
    Dispatched := {};

    \* For each tribe, compute allocation and dispatch jobs
    with k \in KSet do
      if TribeOK(k) then
        \* remaining quota
        variable remainingQuota \in Real;
        remainingQuota := IF Q[k] - U[k] > 0.0 THEN Q[k] - U[k] ELSE 0.0;

        \* planet-gated allocation
        variable alloc \in Real;
        alloc := PlanetGate * remainingQuota;

        \* collect eligible jobs for this tribe
        variable tribeJobs \in SUBSET Jobs;
        tribeJobs := { j \in EligibleJobsPlanet : JobTribe[j] = k };

        \* naive dispatch: pick any subset whose total cost <= alloc
        variable chosen \in SUBSET tribeJobs;
        chosen := { j \in tribeJobs : JobCost[j] <= alloc };

        \* update dispatch set and quota usage
        Dispatched := Dispatched \cup chosen;
        U[k] := U[k] + 
                IF chosen = {} THEN 0.0
                ELSE LET costs == { JobCost[j] : j \in chosen } IN
                     Sum(costs);
      else
        skip;
      end if;
    end with;

    \* remove dispatched jobs from Jobs
    Jobs := Jobs \ Dispatched;

    \* planet dynamics left abstract; could be updated here
    \* E, C, G := E, C, G;

  end while;
end algorithm;
*)

(***************************************************************************)
(* TRANSLATION                                                             *)
(***************************************************************************)

\* The PlusCal translator will generate the TLA+ definitions below.
\* Run: tlc2 / tla2tools on this module to get the expanded spec.

=============================================================================