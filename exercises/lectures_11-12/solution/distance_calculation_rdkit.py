from rdkit import Chem

mol = Chem.MolFromXYZFile(r"/Users/hassanhaydar/DSA103/exercises/lectures_11-12/solution/yne.xyz")
conf = mol.GetConformer()

atom_1_index = 0
atom_2_index = 1
dist = conf.GetAtomPosition(atom_1_index).Distance(conf.GetAtomPosition(atom_2_index))
print(dist)
