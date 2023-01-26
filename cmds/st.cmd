# This should be a test or example startup script

require pdsgo2

epicsEnvSet ("IOCNAME", "ioc05-pdsgo2")

var streamErrorDeadTime 60

iocshLoad("$(pdsgo2_DIR)/pdsgo2.iocsh", ",IP_ADDR=nuc-03,IP_PORT=1140, ASYN_PORT=PORT1")

