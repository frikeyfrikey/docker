from pyzabbix import ZabbixAPI

ZABBIX_SERVER = "https://zabbix.from.sh"

zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login("api_username", "api_password")

triggers = zapi.trigger.get(
    only_true=1,
    skipDependent=1,
    monitored=1,
    active=1,
    output="extend",
    expandDescription=1,
    selectHosts=["host"],
)
