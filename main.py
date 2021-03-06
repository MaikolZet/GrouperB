import DataStructure as dt
import BruteForce as bt
import timeit
import GeneticAlgorithm as ga
import ObjectiveResult as result



struct2 = dt.Structure(3,"Proof/Proof.txt","Proof/ProofNames.txt")
struct2.randomInitialization()
struct2.print()
#struct2.updateX(bt.BruteForce(struct2.y,struct2.n))
#struct2.print()
struct2.updateX(ga.geneticAlgorithm(struct2.y,struct2.n,500))
struct2.print()