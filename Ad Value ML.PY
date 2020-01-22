def weight_considered(height,width,length,gross_weight):

    volumetric = ((height*width*length)/6000)

    if volumetric <= 5:
        weight = gross_weight
        return weight
    else:
        if GrossWeight > volumetric:
            weight = gross_weight
            return weight 
        else:
            weight = volumetric
            return weight


def shipping_cost(product_value,weight):
    cost = 0

    if weight < 0.5:
        cost = 30.90
    elif weight >= 0.5 and weight < 1:
        cost = 33.90
    elif weight >= 1 and weight < 2:
        cost = 34.90
    elif weight >= 2 and weight < 5:
        cost = 43.90
    elif weight >= 5 and weight < 9:
        cost = 63.90
    elif weight >= 9 and weight < 13:
        cost = 99.90
    elif weight >= 13 and weight < 17:
        cost = 110.90
    elif weight >= 17 and weight < 23:
        cost = 129.90
    elif weight >= 23 and weight < 29:
        cost = 149.90
    elif weight > 29:
        cost = 169.90

    if product_value < 120:
        return cost 
    else:
        cost = (cost -(cost*0.4))
        return cost


def commission_inclusion(product_value,classification):
    percentage = 0
    your_worth = product_value

    if classification == True:
        percentage = 16
    else:
        percentage = 11

    while (product_value - ((product_value*percentage)/100) <= your_worth):
        product_value += 0.01
    
    if product_value < 120:
        product_value += 5
        
    return product_value



def Menu():

    product_value = float(input("infome o valor do produto" ))
    height = int(input("infome a altura do produto em cm" ))
    width = int(input("infome a Largura do produto em cm" ))
    length = int(input("infome a Comprimento do produto em cm" ))
    gross_weight = float(input("informe o peso Bruto do Produto em Kg" ))
    weight = weight_considered(height,width,length,gross_weight)

    premium_ad = commission_inclusion(product_value,True)
    classic_ad = commission_inclusion(product_value,False)
    freight = shipping_cost(product_value,weight)
    
    print("")
    print("")
    print("Anúncio Premium:", round((premium_ad+freight),2))
    print("Anúncio Classico:", round((classic_ad+freight),2))


    print("***********************************************************")
    
Menu()
