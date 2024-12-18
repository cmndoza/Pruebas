from zeep import Client
import json
import pandas as pd
from datetime import datetime, timedelta
txt_nss_ws3 = 'dat_nss.txt'
txt_curp_ws3 = 'dat_curp.txt'
nsss = []
curps = []
claves_error_ws1 = []
mensajes_error_ws1 = []
codigos_resultado_ws1 = []
motivos_rechazo_ws1 = []
curp_resp_ws1 = []
primer_apellido_ws1 = []
segundo_apelido_ws1 = []
nombre_ws1 = []
nss_response_ws1 = []
fecha_de_baja_ws1 = []
observaciones_ws1 = []
claves_error_ws3 = []
mensajes_error_ws3 = []
codigos_resultado_ws3 = []
motivos_rechazo_ws3 = []
curp_resp_ws3 = []
primer_apellido_ws3 = []
segundo_apelido_ws3 = []
nombre_ws3 = []
nss_response_ws3 = []
fechas_baja_ws3 = []
observaciones_ws3 = []
fechas_envio_ws3 = []
periodos_portados_ws3 = []
eventos_deduccion_ws3 = []
dias_cotizaddos_ws3 = []
dias_descontados_ws3 = []
dias_reintegrados_ws3 = []
total_dias_ws3 = []
fechas_inicio_ws3 = []
fechas_termino_ws3 = []
nombreDependenciaOPatron_ws3 = []
rps_ws3 = []
entidadFederativaPatron_ws3 = []
sueldoRegistradoPorPeriodo_ws3 = []
tipoMovimiento_ws3 = []
nsss = ['01008122101']
curps = ['PIHA811124MDFXRN02']
# with open(txt_nss_ws3, 'r') as arch_nss:
#     nsss = arch_nss.readlines()
# nsss = [val1.strip() for val1 in nsss]
# with open(txt_curp_ws3, 'r') as arch_curp:
#     curps = arch_curp.readlines()
# curps = [val2.strip() for val2 in curps]
posc = 0
#extension = len(nsss)
extension = 1
while posc <= (extension-1):
    '''VARIABLES INPUT'''
    #nss = str(nsss[posc])
    nss = '01008122101'
    #curp = str(curps[posc])
    curp = 'PIHA811124MDFXRN02'
    inst_recep = str("01")
    fecha = datetime.strftime(datetime.today(), "%d/%m/%Y %H:%M:%S")
    mail = str("carlos.mendoza@syesoftware.com")
    folio = int(12345678901234567890123456789012345678901234567900)
    folio_str = str(folio)
    ########################################################################################################### URL del archivo WSDL del servicio
    wsdl_ws1 = "http://serviciosdigitalesinterno-stage.imss.gob.mx:80/semanascotizadas-rest-ws/WSEstatusAsegurado?wsdl" #DESARROLLO
            # Crear el cliente SOAP
    client_ws1 = Client(wsdl=wsdl_ws1)
            # Llamar a un método del servicio
    response_ws1 = client_ws1.service.getEstatusAsegurado(institutoReceptor=inst_recep,nss=nss,curp=curp,fechaTramite=fecha,correo=mail)
    claves_error_ws1.append(response_ws1['claveError'])
    mensajes_error_ws1.append(response_ws1['mensajeError'])
    codigos_resultado_ws1.append(response_ws1['codigoResultado'])
    motivos_rechazo_ws1.append(response_ws1['motivoRechazo'])
    curp_resp_ws1.append(response_ws1['curp'])
    primer_apellido_ws1.append(response_ws1['primerApellido'])
    segundo_apelido_ws1.append(response_ws1['segundoApellido'])
    nombre_ws1.append(response_ws1['nombre'])
    nss_response_ws1.append(response_ws1['nss'])
    fecha_de_baja_ws1.append(response_ws1['fechaDeBaja'])
    observaciones_ws1.append(response_ws1['observaciones'])
    print(response_ws1)
    if response_ws1['codigoResultado'] == '01':
        wsdl_ws3 = "http://serviciosdigitalesinterno-stage.imss.gob.mx:80/semanascotizadas-rest-ws/WSConsultaPeriodos?wsdl" #DESARROLLO
                # Crear el cliente SOAP
        client_ws3 = Client(wsdl=wsdl_ws3)
                # Llamar a un método del servicio
        response_ws3 = client_ws3.service.getPeriodosAsegurado(institutoReceptor=inst_recep,nss=nss,curp=curp,fechaTramite=fecha,correo=mail,folioTramiteReceptor=folio_str)
        claves_error_ws3.append(response_ws3['claveError'])
        mensajes_error_ws3.append(response_ws3['mensajeError'])
        codigos_resultado_ws3.append(response_ws3['codigoResultado'])
        motivos_rechazo_ws3.append(response_ws3['motivoRechazo'])
        curp_resp_ws3.append(response_ws3['curp'])
        primer_apellido_ws3.append(response_ws3['primerApellido'])
        segundo_apelido_ws3.append(response_ws3['segundoApellido'])
        nombre_ws3.append(response_ws3['nombre'])
        nss_response_ws3.append(response_ws3['nss'])
        fechas_baja_ws3.append(response_ws3['fechaDeBaja'])
        observaciones_ws3.append(response_ws3['observaciones'])
        fechas_envio_ws3.append(response_ws3['fechaDeEnvio'])
        periodos_portados_ws3.append(response_ws3['periodosPortados'])
        eventos_deduccion_ws3.append(response_ws3['eventosDeduccion'])
        dias_cotizaddos_ws3.append(response_ws3['diasCotizados'])
        dias_descontados_ws3.append(response_ws3['diasDescontados'])
        dias_reintegrados_ws3.append(response_ws3['diasReintegrados'])
        total_dias_ws3.append(response_ws3['totalDeDias'])
        lista_periodos_ws3 = response_ws3['listaPeriodos']
        for periodos_ws3 in lista_periodos_ws3:
            fechas_inicio_ws3.append(f"{periodos_ws3['fechaInicio']}")
            fechas_termino_ws3.append(f"{periodos_ws3['fechaTermino']}")
            nombreDependenciaOPatron_ws3.append(f"{periodos_ws3['nombreDependenciaOPatron']}")
            rps_ws3.append(f"{periodos_ws3['RP']}")
            entidadFederativaPatron_ws3.append(f"{periodos_ws3['entidadFederativaPatron']}")
            sueldoRegistradoPorPeriodo_ws3.append(f"{periodos_ws3['sueldoRegistradoPorPeriodo']}")
            tipoMovimiento_ws3.append(f"{periodos_ws3['tipoMovimiento']}")
        #print (response_ws3)
    posc = posc + 1
    print ("Ahí voy, ¬.¬ Llevo", posc, "de", extension)

resultados_ws1  = {'nss_capturada':nsss, 'curp_capturada':curps, 'clave_de_error':claves_error_ws1,'mensaje_de_error':mensajes_error_ws1,
               'cod_resultado':codigos_resultado_ws1,'motivo_de_rechazo':motivos_rechazo_ws1,'curp_response':curp_resp_ws1,'primer_apellido':primer_apellido_ws1,
               'segundo_apellido':segundo_apelido_ws1,'nombre':nombre_ws1,'nss_response':nss_response_ws1,'fecha_de_baja':fecha_de_baja_ws1,
               'observaciones':observaciones_ws1}
resultados_ws3  = {'nss_capturada':nsss, 'curp_capturada':curps, 'clave_de_error':claves_error_ws3,'mensaje_de_error':mensajes_error_ws3,
               'cod_resultado':codigos_resultado_ws3,'motivo_de_rechazo':motivos_rechazo_ws3,'curp_response':curp_resp_ws3,'primer_apellido':primer_apellido_ws3,
               'segundo_apellido':segundo_apelido_ws3,'nombre':nombre_ws3,'nss_response':nss_response_ws3,'fecha_de_baja':fechas_baja_ws3,
               'observaciones':observaciones_ws3, 'Fecha de Envio':fechas_envio_ws3, 'Periodos portados':periodos_portados_ws3, 'Eventos de Retiro': eventos_deduccion_ws3,
               'Dias Cotizados':dias_cotizaddos_ws3, 'Días Descontados': dias_descontados_ws3, 'Dias Reintegrados': dias_reintegrados_ws3, 'Dias Netos': total_dias_ws3}
periodos_ws3= {'Fecha Inicio': fechas_inicio_ws3, 'Fecha fin': fechas_termino_ws3, 'Nombre Patron': nombreDependenciaOPatron_ws3, 'RP': rps_ws3, 'estado': entidadFederativaPatron_ws3,
               'Salario': sueldoRegistradoPorPeriodo_ws3, 'Tipo Movs': tipoMovimiento_ws3}
matriz_resultados_ws1 = pd.DataFrame(resultados_ws1)
matriz_resultados_ws3 = pd.DataFrame(resultados_ws3)
matriz_periodos_ws3 = pd.DataFrame(periodos_ws3)
matriz_resultados_ws1.to_csv('resultados_ws1_3.txt', index=False, sep='|')
matriz_resultados_ws3.to_csv('resultados_ws3_3.txt', index=False, sep='|')
matriz_periodos_ws3.to_csv('periodos_ws3_3.txt', index=False, sep='|')