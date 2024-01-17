from pyzabbix import ZabbixAPI

ZABBIX_SERVER = "https://zabbix.from.sh"

zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login("api_username", "api_password")

trigger=zapi.trigger.get()
