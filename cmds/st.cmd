# This should be a test or example startup script

require pdsgo2

epicsEnvSet ("IOCNAME", "ioc05-pdsgo2")

iocshLoad("$(pdsgo2_DIR)/pdsgo2.iocsh", ",IP_ADDR=localhost,IP_PORT=1140, ASYN_PORT=PORT1")

