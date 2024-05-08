''' This module provides a reusable byline for the author's services. '''

# Import Dependencies
import math
import statistics

def main():
    

    # Define Variables
    company_name: str = 'Saint Louis Farms'
    company_description: str = 'Farm to table company based out of Saint Louis'
    company_founding_year: int = 1995
    company_city: str = 'St Louis'
    company_state: str = 'Missouri'
    company_number_employees: int = 5000
    company_offers_benefits: bool = True
    products_offered: list = ['milk', 'eggs', 'cheese', 'butter']
    product_price: list = [4, 3, 5, 2]
    company_sourced_outside_US: bool = False
    company_public_stock: bool = True
    company_stock_price: float = 328.91

# Multiline string with byline using f-string formatting
    byline: str = f"""
    Information:
    Name: {company_name}
    Description: {company_description}
    Founding Year: {company_founding_year}
    City: {company_city}
    State: {company_state}
    Number of Employees: {company_number_employees}
    Employee Benefits: {company_offers_benefits}

    Products With Pricing:
    Products Offered: {products_offered}
    Product Price: {product_price}
    Max Product Price: {max(product_price)}
    Min Product Price: {min(product_price)}
    Mean Product Price: {statistics.mean(product_price)}
    Median Product Price: {statistics.median(product_price)}
    Standard Deviation of Product Price: {statistics.stdev(product_price)}
    Public Stock: {company_public_stock}
    Stock Price: ${company_stock_price}
    """

    print(byline)

# Call the main function to execute the code
if __name__ == '__main__':
    main()
