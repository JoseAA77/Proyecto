# El programa es comunicarà entre plaques mitjançanmt un diccionari on s'enviarà la part del diccionari que s'hagi modificat entre les 
#plaques. Cada x segons o minuts, s'enviarà el diccionari complert per a comprovar que estigui tot actualitzat (poder una versió següent)
# El programa compararà el diccionari anterior, mitjançant un sort i la creació d'una llista, amb l'actual i compararà si ho ha algun 
#canvi. Si són iguals ignorarà les llibreries i no farà res. Si no és igual, realitzarà l'acció que hagi de fer per a actualitzar
#l'estat dels components.
# També o en substitució, l'alterrnativa seria que agafés una variable buida en la que si ho ha un canvi en algún sensor o en alguna 
#acció cap a un actuador, aquesta variable estarà plena amb el canvi a realitzar i actuarà en consequwencia el sistema, per exemple amb una
#referència del q s'està modificant.

#estat_casa = { llum_menjador : {llums,5}, llum_cuina : {llums,0}, sensor_gas : {gas,0}, estat_alarma : {alarma,{"armada","desactivada"}}}
#estat_casa = { llum : {menjador : 5}, llum : {cuina : 0}, gas : {mq135 : 0}, {alarma : {alarma : {"armada","desactivada"}}}
#keys_estat_casa = { llum : "llum", gas : "gas", alarma : "alarma"}
#estat_casa = { llum_menjador : 5, llum_cuina : 0, gas_cuina : 0, alarma_general : {"armada","desactivada"}}
objecte_casa = { llum_menjador : pcaLM, llum_cuina : pcaLC, gas_cuina : mq1351, alarma_general : alarmaG}
estat_casa = { llum_menjador : "5T" '''(aixó seria valor 5% i True, és a dir encés. Si fos F, seria apagat (False))''', llum_cuina : 0, gas_cuina : 0, alarma_general : {"armada","desactivada"}}

estat_casa = { "llum_menjador" : {"estat" : 5, "objecte" : llum_M}, "alarmaGeneral": {"estat": "activada", "armada" : True, "objecte": "alarmaGeneral"},

#En una primera versió, enviarem només el diccionari dinàmic, la part del diccionari estatic la posarem en un diccionari intern de cada placa.

import re

rebut = "'{ llum_menjador : '5T' , llum_cuina : '100F', gas_cuina : 0, alarma_general : 'ArmDes'}}"
                                                                                ArmadaDesactivada 
                                                                                DesDes/DesAct/ArmAct
                                                            DesarmadaDesactivada/DesarmadaActivada/ArmadaActivada
# diccionaris estàtics
objectes_casa = {
                "Llum_Cuina" : Llum_Cuina_PCA,
                "Llum_Passadis" : Llum_Passadis_PCA,
                "Llum_Menjador" : Llum_Menjador_PCA,
                "Llum_Lavabo" : Llum_Lavabo_PCA,
                "Llum_Habitació_1" : Llum_Habitació_1,
                "Llum_Habitació_2" : Llum_Habitació_2,
                "Llum_Habitació_3" : Llum_Habitació_3,
                
                "Pols_Llum_Cuina" : Pols_Llum_Cuina_PCA,
                "Pols_Llum_Passadis" : Pols_Llum_Passadis_PCA,
                "Pols_Llum_Menjador" : Pols_Llum_Menjador_PCA,
                "Pols_Llum_Lavabo" : Pols_Llum_Lavabo_PCA,
                "Pols_Llum_Habitacio_1" : Pols_Llum_Habitacio_1,
                "Pols_Llum_Habitacio_2" : Pols_Llum_Habitacio_2,
                "Pols_Llum_Habitacio_3" : Pols_Llum_Habitacio_3,
                
                "Proximitat_Passadis" : Proximitat_Passadis,
                "Proximitat_Menjador" : Proximitat_Menjador,
                "Proximitat_Habitacio_2" : Proximitat_Habitacio_2,
                "Proximitat_Habitacio_3" : Proximitat_Habitacio_3,
                
                "Reed_PEntrada" : Reed_PEntrada,
                "Reed_Menjador" : Reed_Menjador,
                "Reed_Habitacio_2" : Reed_Habitacio_2,
                "Reed_Habitacio_3" : Reed_Habitacio_3,
                
                "Gas_MQ135" : Gas_MQ135
                }

# diccionaris dinàmics
            
import re

def to_diccionari (text):
    # Regex per capturar la clau i el valor
    pattern = r'(\w+)\s*:\s*({.*?}|\d+|"[^"]*")'
    matches = re.findall(pattern, text)
    
    # Crear el diccionari
    diccionari = {}
    for key, value in matches:
        if value.startswith("{"):  # Si el valor és un conjunt (set)
            diccionari[key] = set(value.strip("{}").split(","))
        elif value.isdigit():  # Si el valor és un número
            diccionari[key] = int(value)
        else:  # Si el valor és una cadena de text
            diccionari[key] = value.strip('"')
            
    return (diccionari)

novetat = to_diccionari(rebut)
claus_novetat = novetat.keys()



'''
#######
estat_complet = {
    "llum": {"estat": "ON", "objecte": "menjador"},
    "gas": {"estat": "OFF", "objecte": "cuina"},
    "alarma": {"estat": "activada", "objecte": "dormitori"},
}

# Accés fàcil a tots els atributs
for clau, dades in estat_complet.items():
    print(f"{clau.capitalize()} està {dades['estat']} a {dades['objecte']}")
-> Llum està ON a menjador
Gas està OFF a cuina
Alarma està activada a dormitori

##
# Canviar l'estat de la llum
estat_complet["llum"]["estat"] = "OFF"

# Afegir un nou atribut
estat_complet["llum"]["intensitat"] = 75

# Resultat
print(estat_complet["llum"])
-> {'estat': 'OFF', 'objecte': 'menjador', 'intensitat': 75}


######
estat_casa[llum_menjador] = 3

if lum_menjador:
    pca.encen("menjador",3)   
    
envia = {llum_cuina : 6}

estat_casa[llum_cuina] = 6
'''