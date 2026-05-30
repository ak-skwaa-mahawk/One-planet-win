----------------------------- MODULE PlanetGatedScheduler -----------------------------

EXTENDS Naturals, Reals, Sequences

(***************************************************************************)
(* CONSTANTS                                                              *)
(***************************************************************************)

CONSTANTS
    K              \* planet gate gain > 0
    EMax, CMax, GMax \* planet limits
    EpsP           \* tolerance for P = 1
    DeltaP         \* planetary tube radius
    KSet           \* set of tribes
    Q              \* [KSet -> Real] tribe quotas
    WBar           \* planet-weight threshold for emergency mode (0 < WBar <= 1)

(***************************************************************************)
(* STATE VARIABLES                                                        *)
(***************************************************************************)

VARIABLES
    E, C, G,       \* planet state components
    U,             \* [KSet -> Real] used quota per tribe
    Jobs,          \* set of job ids
    JobTribe,      \* [Jobs -> KSet]
    JobCost,       \* [Jobs -> Real]
    JobPriority,   \* [Jobs -> Real]
    JobWeight,     \* [Jobs -> Real] in [0,1]
    JobValid,      \* [Jobs -> BOOLEAN] individual validity I_j
    Dispatched     \* subset of Jobs dispatched in this step

(***************************************************************************)
(* HELPER DEFINITIONS                                                     *)
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
(* INITIAL STATE                                                          *)
(***************************************************************************)

Init ==
    /\ E \in Real
    /\ C \in Real
    /\ G \in Real
    /\ U \in [KSet -> Real]
    /\ Jobs \subseteq DOMAIN JobTribe
    /\ JobTribe \in [Jobs -> KSet]
    /\ JobCost \in [Jobs -> Real]
    /\ JobPriority \in [Jobs -> Real]
    /\ JobWeight \in [Jobs -> Real]
    /\ JobValid \in [Jobs -> BOOLEAN]
    /\ Dispatched = {} 

(***************************************************************************)
(* NEXT-STEP RELATION                                                     *)
(***************************************************************************)

(*
   We abstract the actual scheduling algorithm as any choice of Dispatched
   that respects:
   - planet gate (total cost per tribe <= PlanetGate * remaining quota)
   - tribe quotas
   - individual validity
   - emergency filter when PlanetOK = FALSE
*)

Next ==
    \E Dispatched' \subseteq Jobs:
        /\ Dispatched' \subseteq EligibleJobsPlanet
        /\ \A k \in KSet:
              LET tribeJobs == { j \in Dispatched' : JobTribe[j] = k } IN
              LET totalCost == IF tribeJobs = {} THEN 0.0
                               ELSE Sum({ JobCost[j] : j \in tribeJobs })
              IN  /\ totalCost <= PlanetGate * Max(0.0, Q[k] - U[k])
                  /\ U'[k] = U[k] + totalCost
        /\ Jobs' = Jobs \ { j \in Dispatched' }
        /\ Dispatched' = Dispatched
        /\ UNCHANGED <<E, C, G, JobTribe, JobCost, JobPriority, JobWeight, JobValid>>

(***************************************************************************)
(* INVARIANTS                                                             *)
(***************************************************************************)

(*
   1. Boolean hierarchy:
      - No dispatched job violates individual validity.
      - No tribe exceeds quota.
      - In emergency mode, only high-planet-weight jobs are dispatched.
*)

Inv_IndividualValidity ==
    \A j \in Dispatched: IndOK(j)

Inv_TribeQuota ==
    \A k \in KSet: U[k] <= Q[k]

Inv_EmergencyFilter ==
    ~PlanetOK => \A j \in Dispatched: JobWeight[j] >= WBar

(*
   2. Planetary tube (soft): we require the system to remain within a
      bounded error region. In practice, this is enforced by the environment
      dynamics, but we state it as a desired invariant.
*)

Inv_PlanetTube ==
    Norm2(PlanetError) <= DeltaP

(***************************************************************************)
(* SPECIFICATION                                                          *)
(***************************************************************************)

Spec ==
    Init /\ [][Next]_<<E, C, G, U, Jobs, Dispatched>>

Safety ==
    Inv_IndividualValidity /\ Inv_TribeQuota /\ Inv_EmergencyFilter

=============================================================================