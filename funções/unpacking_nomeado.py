def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

podium = {'segundo': 'M. Verstappen', 
             'primeiro': 'L. Hamilton',
             'terceiro': 'S. Vettel'}

resultado_f1(**podium)