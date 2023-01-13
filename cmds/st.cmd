# This should be a test or example startup script

require pdsgo2

epicsEnvSet ("IOCNAME", "ioc05-pdsgo2")

iocshLoad("$(pdsgo2_DIR)/pdsgo2.iocsh", "SERIAL_PORT=/dev/ttyUSB0")

