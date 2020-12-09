class FeatureRecipe:
    """ TODO : __init__ """

    def separate_variable_types(self) -> None:
        """ TODO : Diviser les types de variables dans un tableau """
        pass
    
    def drop_uselessf(self):
        """ TODO : Supprimer les colonnes inutiles du dataset """
        pass
    
    def deal_duplicate(self):
        """ TODO : Supprimer les lignes dupliquées du dataset """
        pass
    
    def drop_nanp(self, threshold: float):
        """ TODO : Supprimer un pourcentage de NA du dataset """
        pass
    
    def deal_dtime(self):
        """ TODO : Traiter les DateTime """
        pass

    def prepare_data(self, threshold: float):
        self.separate_variable_types()
        self.drop_uselessf()
        self.deal_duplicate()
        self.drop_nanp(threshold)
        self.deal_dtime()