import pandas as pd

class DataHandler:
    def __init__(self):
        self.data_merge = None
        self.price_availability = None
        self.listing_final = None


    def get_data(self):
        self.listing_final = pd.read_csv("data/listings_final.csv", sep = ";")
        self.price_availability = pd.read_csv("data/price_availability.csv", sep = ";")

    def group_data(self):
        self.data_merge = pd.merge(self.listing_final, self.price_availability.groupby('listing_id')['local_price'].mean('local_price'),how='inner', on='listing_id')

    def get_process_data(self):
        self.get_data()
        self.group_data()