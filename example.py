from pyql.weather.models import GeoData, Weather

lat = "21.143185"
long = "-88.151035"



def main(lat,long):
    print "================================="
    print "obteniendo datos geoespaciales (%s, %s) ...." %(lat, long)
    print "================================="
    geo = GeoData(lat, long) # Inicializamos el objeto
    print "El WOEID = %s"%str(geo.get_woeid())
    print "%s, %s, %s"%(str(geo.get_city().encode('utf-8')), str(geo.get_state().encode('utf-8')), str(geo.get_country().encode('utf-8')))
    print "================================="
    print "consultando clima actual........"
    print "================================="
    w = Weather(geo.get_woeid())
    print "Temperatura: %sc. Estatus: (%s) %s"%(w.get_temperature(), w.get_status_code(), w.get_status_text())


main(lat,long)