from zeep import Client
import json
import pandas as pd
#import numpy as np
from datetime import datetime, timedelta
txt_nss = 'dat_nss.txt'
txt_curp = 'dat_curp.txt'
nsss = []
curps = []
claves_error = []
mensajes_error = []
codigos_resultado = []
motivos_rechazo = []
curp_resp = []
primer_apellido = []
segundo_apelido = []
nombre = []
nss_response = []
fecha_de_baja = []
observaciones = []
with open(txt_nss, 'r') as arch_nss:
    nsss = arch_nss.readlines()
nsss = [val1.strip() for val1 in nsss]
with open(txt_curp, 'r') as arch_curp:
    curps = arch_curp.readlines()
curps = [val2.strip() for val2 in curps]
posc = 0
while posc <= len(nsss)-1:
    '''VARIABLES INPUT'''
    nss = str(nsss[posc])
    curp = str(curps[posc])
    inst = str("01")
    fecha = str("18/12/2024 00:00:00")
    mail = str("carlos.mendoza@syesoftware.com")
    ########################################################################################################### URL del archivo WSDL del servicio
    #wsdl = "http://172.16.23.206:80/WSCuentaIndividualSISEC/WSCuentaIndividualSISEC?wsdl" #PRODUCCION
    wsdl = "http://serviciosdigitalesinterno-stage.imss.gob.mx:80/semanascotizadas-rest-ws/WSEstatusAsegurado?wsdl" #DESARROLLO
            # Crear el cliente SOAP
    client = Client(wsdl=wsdl)
            # Llamar a un método del servicio
    response = client.service.getEstatusAsegurado(institutoReceptor=inst,nss=nss,curp=curp,fechaTramite=fecha,correo=mail)
    claves_error.append(response['claveError'])
    mensajes_error.append(response['mensajeError'])
    codigos_resultado.append(response['codigoResultado'])
    motivos_rechazo.append(response['motivoRechazo'])
    curp_resp.append(response['curp'])
    primer_apellido.append(response['primerApellido'])
    segundo_apelido.append(response['segundoApellido'])
    nombre.append(response['nombre'])
    nss_response.append(response['nss'])
    fecha_de_baja.append(response['fechaDeBaja'])
    observaciones.append(response['observaciones'])
    #print(response)
    posc = posc + 1
resultados  = {'nss_capturada':nsss, 'curp_capturada':curps, 'clave_de_error':claves_error,'mensaje_de_error':mensajes_error,
               'cod_resultado':codigos_resultado,'motivo_de_rechazo':motivos_rechazo,'curp_response':curp_resp,'primer_apellido':primer_apellido,
               'segundo_apellido':segundo_apelido,'nombre':nombre,'nss_response':nss_response,'fecha_de_baja':fecha_de_baja,
               'observaciones':observaciones}
matriz_resultados = pd.DataFrame(resultados)
matriz_resultados.to_csv('resultados_ws1.txt', index=False, sep='\t')