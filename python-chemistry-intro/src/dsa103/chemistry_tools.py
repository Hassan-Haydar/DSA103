from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


def calculate_molecular_formula(smiles: str) -> float:
    """Calculates the molecular formula for a given molecule. The molecule is expected to be a Smiles string."""
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.")

    return rdMolDescriptors.CalcMolFormula(mol)


def calculate_molecular_weight(smiles: str) -> float:
    """
    Calculates the exact molecular weight for a given molecule.
    The molecule is expected to be provided as a SMILES string.

    Args:
        smiles (str): The SMILES representation of the molecule.

    Returns:
        float: The exact molecular weight of the molecule.

    Raises:
        ValueError: If the SMILES string is invalid and cannot be parsed.
    """
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.")

    return rdMolDescriptors.CalcExactMolWt(mol)


def calculate_molecular_weight(molecule: str) -> float:
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.")

    return rdMolDescriptors.CalcExactMolWt(mol)
