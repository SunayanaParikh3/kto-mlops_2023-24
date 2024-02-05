import unittest

def count_names_with_length_above_threshold(names: list[str], length_threshold: int = 7) -> int:
    """
    Compte le nombre de noms ayant plus de 'length_threshold' caractères.

    Args:
    - names: Liste des noms à évaluer.
    - length_threshold: Seuil de longueur des noms à compter.

    Returns:
    - Nombre de noms dépassant le seuil de longueur spécifié.
    """
    count_above_threshold = 0
    for name in names:
        if len(name) > length_threshold:
            count_above_threshold += 1
            print(f"Prenom supérieur à {length_threshold} : {name}")
        else:
            print(f"Prenom inférieur ou égal à {length_threshold} : {name}")
    return count_above_threshold


class TestNamesMethod(unittest.TestCase):
    def test_names_with_length_above_threshold(self):
        # Liste de prénoms à tester
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        
        # Appel de la fonction avec la liste de prénoms
        count_above_threshold = count_names_with_length_above_threshold(names=names_list)
        
        # Valeur attendue pour le nombre de prénoms dépassant le seuil
        expected_count = 4

        # Vérification que le résultat obtenu correspond à la valeur attendue
        self.assertEqual(count_above_threshold, expected_count)

if __name__ == '__main__':
    unittest.main()