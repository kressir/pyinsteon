"""Constants used to ensure topic consistantancy."""

STANDARD_RECEIVED = 'standard_received'
EXTENDED_RECEIVED = 'extended_received'
X10_RECEIVED = 'x10_received'
ALL_LINKING_COMPLETED = 'all_linking_completed'
BUTTON_EVENT_REPORT = 'button_event_report'
USER_RESET_DETECTED = 'user_reset_detected'
ALL_LINK_CLEANUP_FAILURE_REPORT = 'all_link_cleanup_failure_report'
ALL_LINK_RECORD_RESPONSE = 'all_link_record_response'
ALL_LINK_CLEANUP_STATUS_REPORT = 'all_link_cleanup_status_report'
GET_IM_INFO = 'get_im_info'
SEND_ALL_LINK_COMMAND = 'send_all_link_command'
SEND_STANDARD = 'send_standard'
SEND_EXTENDED = 'send_extended'
X10_SEND = 'x10_send'
START_ALL_LINKING = 'start_all_linking'
CANCEL_ALL_LINKING = 'cancel_all_linking'
SET_HOST_DEV_CAT = 'set_host_dev_cat'
RESET_IM = 'reset_im'
SET_ACK_MESSAGE_BYTE = 'set_ack_message_byte'
GET_FIRST_ALL_LINK_RECORD = 'get_first_all_link_record'
GET_NEXT_ALL_LINK_RECORD = 'get_next_all_link_record'
SET_IM_CONFIGURATION = 'set_im_configuration'
GET_ALL_LINK_RECORD_FOR_SENDER = 'get_all_link_record_for_sender'
LED_ON = 'led_on'
LED_OFF = 'led_off'
MANAGE_ALL_LINK_RECORD = 'manage_all_link_record'
SET_NAK_MESSAGE_BYTE = 'set_nak_message_byte'
SET_ACK_MESSAGE_TWO_BYTES = 'set_ack_message_two_bytes'
RF_SLEEP = 'rf_sleep'
GET_IM_CONFIGURATION = 'get_im_configuration'
#Command Topics
ASSIGN_TO_ALL_LINK_GROUP = 'assign_to_all_link_group'
DELETE_FROM_ALL_LINK_GROUP = 'delete_from_all_link_group'
PRODUCT_DATA_REQUEST = 'product_data_request'
FX_USERNAME = 'fx_username'
DEVICE_TEXT_STRING_REQUEST = 'device_text_string_request'
SET_DEVICE_TEXT_STRING = 'set_device_text_string'
SET_ALL_LINK_COMMAND_ALIAS = 'set_all_link_command_alias'
SET_ALL_LINK = 'set_all_link'
ENTER_LINKING_MODE = 'enter_linking_mode'
ENTER_UNLINKING_MODE = 'enter_unlinking_mode'
GET_INSTEON_ENGINE_VERSION = 'get_insteon_engine_version'
PING = 'ping'
ID_REQUEST = 'id_request'
ID_REQUEST_RESPONSE = 'id_request_response'
ON = 'on'
ON_FAST = 'on_fast'
OFF = 'off'
OFF_FAST = 'off_fast'
BRIGHTEN_ONE_STEP = 'brighten_one_step'
DIM_ONE_STEP = 'dim_one_step'
START_MANUAL_CHANGE_DOWN = 'start_manual_change_down'
START_MANUAL_CHANGE_UP = 'start_manual_change_up'
STOP_MANUAL_CHANGE = 'stop_manual_change'
STATUS_REQUEST = 'status_request'
STATUS_REQUEST_ALTERNATE_1 = 'status_request_alternate_1'
STATUS_REQUEST_ALTERNATE_2 = 'status_request_alternate_2'
STATUS_REQUEST_ALTERNATE_3 = 'status_request_alternate_3'
STATUS_REQUEST_ALTERNATE_ALL = 'status_request_alternate_all'
GET_OPERATING_FLAGS = 'get_operating_flags'
SET_OPERATING_FLAGS = 'set_operating_flags'
INSTANT_CHANGE = 'instant_change'
MANUALLY_TURNED_OFF = 'manually_turned_off'
MANUALLY_TURNED_ON = 'manually_turned_on'
REMOTE_SET_BUTTON_TAP1_TAP = 'remote_set_button_tap1_tap'
REMOTE_SET_BUTTON_TAP2_TAP = 'remote_set_button_tap2_tap'
SET_STATUS = 'set_status'
SET_ADDRESS_MSB = 'set_address_msb'
POKE_ONE_BYTE = 'poke_one_byte'
PEEK_ONE_BYTE = 'peek_one_byte'
PEEK_ONE_BYTE_INTERNAL = 'peek_one_byte_internal'
POKE_ONE_BYTE_INTERNAL = 'poke_one_byte_internal'
ON_AT_RAMP_RATE = 'on_at_ramp_rate'
EXTENDED_GET_SET = 'extended_get_set'
OFF_AT_RAMP_RATE = 'off_at_ramp_rate'
EXTENDED_READ_WRITE_ALDB = 'extended_read_write_aldb'
EXTENDED_TRIGGER_ALL_LINK = 'extended_trigger_all_link'
SPRINKLER_VALVE_ON = 'sprinkler_valve_on'
SPRINKLER_VALVE_OFF = 'sprinkler_valve_off'
SPRINKLER_PROGRAM_ON = 'sprinkler_program_on'
SPRINKLER_PROGRAM_OFF = 'sprinkler_program_off'
SPRINKLER_LOAD_INITIALIZATION_VALUES = 'sprinkler_load_initialization_values'
SPRINKLER_LOAD_EEPROM_FROM_RAM = 'sprinkler_load_eeprom_from_ram'
SPRINKLER_GET_VALVE_STATUS = 'sprinkler_get_valve_status'
SPRINKLER_INHIBIT_COMMAND_ACCEPTANCE = 'sprinkler_inhibit_command_acceptance'
SPRINKLER_RESUME_COMMAND_ACCEPTANCE = 'sprinkler_resume_command_acceptance'
SPRINKLER_SKIP_FORWARD = 'sprinkler_skip_forward'
SPRINKLER_SKIP_BACK = 'sprinkler_skip_back'
SPRINKLER_ENABLE_PUMP_ON_V8 = 'sprinkler_enable_pump_on_v8'
SPRINKLER_DISABLE_PUMP_ON_V8 = 'sprinkler_disable_pump_on_v8'
SPRINKLER_BROADCAST_ON = 'sprinkler_broadcast_on'
SPRINKLER_BROADCAST_OFF = 'sprinkler_broadcast_off'
SPRINKLER_LOAD_RAM_FROM_EEPROM = 'sprinkler_load_ram_from_eeprom'
SPRINKLER_SENSOR_ON = 'sprinkler_sensor_on'
SPRINKLER_SENSOR_OFF = 'sprinkler_sensor_off'
SPRINKLER_DIAGNOSTICS_ON = 'sprinkler_diagnostics_on'
SPRINKLER_DIAGNOSTICS_OFF = 'sprinkler_diagnostics_off'
SPRINKLER_GET_PROGRAM_REQUEST = 'sprinkler_get_program_request'
IO_OUTPUT_ON = 'io_output_on'
IO_OUTPUT_OFF = 'io_output_off'
IO_ALARM_DATA_REQUEST = 'io_alarm_data_request'
IO_WRITE_OUTPUT_PORT = 'io_write_output_port'
IO_READ_INPUT_PORT = 'io_read_input_port'
IO_GET_SENSOR_VALUE = 'io_get_sensor_value'
IO_SET_SENSOR_1_NOMINAL_VALUE = 'io_set_sensor_1_nominal_value'
IO_GET_SENSOR_ALARM_DELTA = 'io_get_sensor_alarm_delta'
FAN_STATUS_REPORT = 'fan_status_report'
IO_WRITE_CONFIGURATION_PORT = 'io_write_configuration_port'
IO_READ_CONFIGURATION_PORT = 'io_read_configuration_port'
IO_MODULE_LOAD_INITIALIZATION_VALUES = 'io_module_load_initialization_values'
IO_MODULE_LOAD_EEPROM_FROM_RAM = 'io_module_load_eeprom_from_ram'
IO_MODULE_STATUS_REQUEST = 'io_module_status_request'
IO_MODULE_READ_ANALOG_ONCE = 'io_module_read_analog_once'
IO_MODULE_READ_ANALOG_ALWAYS = 'io_module_read_analog_always'
IO_MODULE_ENABLE_STATUS_CHANGE_MESSAGE = 'io_module_enable_status_change_message'
IO_MODULE_DISABLE_STATUS_CHANGE_MESSAGE = 'io_module_disable_status_change_message'
IO_MODULE_LOAD_RAM_FROM_EEPROM = 'io_module_load_ram_from_eeprom'
IO_MODULE_SENSOR_ON = 'io_module_sensor_on'
IO_MODULE_SENSOR_OFF = 'io_module_sensor_off'
IO_MODULE_DIAGNOSTICS_ON = 'io_module_diagnostics_on'
IO_MODULE_DIAGNOSTICS_OFF = 'io_module_diagnostics_off'
POOL_DEVICE_ON = 'pool_device_on'
POOL_DEVICE_OFF = 'pool_device_off'
POOL_TEMPERATURE_UP = 'pool_temperature_up'
POOL_TEMPERATURE_DOWN = 'pool_temperature_down'
POOL_LOAD_INITIALIZATION_VALUES = 'pool_load_initialization_values'
POOL_LOAD_EEPROM_FROM_RAM = 'pool_load_eeprom_from_ram'
POOL_GET_POOL_MODE = 'pool_get_pool_mode'
POOL_GET_AMBIENT_TEMPERATURE = 'pool_get_ambient_temperature'
POOL_GET_WATER_TEMPERATURE = 'pool_get_water_temperature'
POOL_GET_PH = 'pool_get_ph'
DOOR_MOVE_RAISE_DOOR = 'door_move_raise_door'
DOOR_MOVE_LOWER_DOOR = 'door_move_lower_door'
DOOR_MOVE_OPEN_DOOR = 'door_move_open_door'
DOOR_MOVE_CLOSE_DOOR = 'door_move_close_door'
DOOR_MOVE_STOP_DOOR = 'door_move_stop_door'
DOOR_MOVE_SINGLE_DOOR_OPEN = 'door_move_single_door_open'
DOOR_MOVE_SINGLE_DOOR_CLOSE = 'door_move_single_door_close'
DOOR_STATUS_REPORT_RAISE_DOOR = 'door_status_report_raise_door'
DOOR_STATUS_REPORT_LOWER_DOOR = 'door_status_report_lower_door'
DOOR_STATUS_REPORT_OPEN_DOOR = 'door_status_report_open_door'
DOOR_STATUS_REPORT_CLOSE_DOOR = 'door_status_report_close_door'
DOOR_STATUS_REPORT_STOP_DOOR = 'door_status_report_stop_door'
DOOR_STATUS_REPORT_SINGLE_DOOR_OPEN = 'door_status_report_single_door_open'
DOOR_STATUS_REPORT_SINGLE_DOOR_CLOSE = 'door_status_report_single_door_close'
WINDOW_COVERING_OPEN = 'window_covering_open'
WINDOW_COVERING_CLOSE = 'window_covering_close'
WINDOW_COVERING_STOP = 'window_covering_stop'
WINDOW_COVERING_PROGRAM = 'window_covering_program'
WINDOW_COVERING_POSITION = 'window_covering_position'
THERMOSTAT_TEMPERATURE_UP = 'thermostat_temperature_up'
THERMOSTAT_TEMPERATURE_DOWN = 'thermostat_temperature_down'
THERMOSTAT_GET_ZONE_INFORMATION = 'thermostat_get_zone_information'
THERMOSTAT_LOAD_INITIALIZATION_VALUES = 'thermostat_load_initialization_values'
THERMOSTAT_LOAD_EEPROM_FROM_RAM = 'thermostat_load_eeprom_from_ram'
THERMOSTAT_GET_MODE = 'thermostat_get_mode'
THERMOSTAT_GET_AMBIENT_TEMPERATURE = 'thermostat_get_ambient_temperature'
THERMOSTAT_ON_HEAT = 'thermostat_on_heat'
THERMOSTAT_ON_COOL = 'thermostat_on_cool'
THERMOSTAT_ON_AUTO = 'thermostat_on_auto'
THERMOSTAT_ON_FAN = 'thermostat_on_fan'
THERMOSTAT_OFF_FAN = 'thermostat_off_fan'
THERMOSTAT_OFF_ALL = 'thermostat_off_all'
THERMOSTAT_PROGRAM_HEAT = 'thermostat_program_heat'
THERMOSTAT_PROGRAM_COOL = 'thermostat_program_cool'
THERMOSTAT_PROGRAM_AUTO = 'thermostat_program_auto'
THERMOSTAT_GET_EQUIPMENT_STATE = 'thermostat_get_equipment_state'
THERMOSTAT_SET_EQUIPMENT_STATE = 'thermostat_set_equipment_state'
THERMOSTAT_GET_TEMPERATURE_UNITS = 'thermostat_get_temperature_units'
THERMOSTAT_SET_FAHRENHEIT = 'thermostat_set_fahrenheit'
THERMOSTAT_SET_CELSIUS = 'thermostat_set_celsius'
THERMOSTAT_GET_FAN_ON_SPEED = 'thermostat_get_fan_on_speed'
THERMOSTAT_SET_FAN_ON_SPEED_LOW = 'thermostat_set_fan_on_speed_low'
THERMOSTAT_SET_FAN_ON_SPEED_MEDIUM = 'thermostat_set_fan_on_speed_medium'
THERMOSTAT_SET_FAN_ON_SPEED_HIGH = 'thermostat_set_fan_on_speed_high'
THERMOSTAT_ENABLE_STATUS_CHANGE_MESSAGE = 'thermostat_enable_status_change_message'
THERMOSTAT_DISABLE_STATUS_CHANGE_MESSAGE = 'thermostat_disable_status_change_message'
THERMOSTAT_SET_COOL_SETPOINT = 'thermostat_set_cool_setpoint'
THERMOSTAT_SET_HEAT_SETPOINT = 'thermostat_set_heat_setpoint'
THERMOSTAT_TEMPERATURE_STATUS = 'thermostat_temperature_status'
THERMOSTAT_HUMIDITY_STATUS = 'thermostat_humidity_status'
THERMOSTAT_MODE_STATUS = 'thermostat_mode_status'
THERMOSTAT_COOL_SET_POINT_STATUS = 'thermostat_cool_set_point_status'
THERMOSTAT_HEAT_SET_POINT_STATUS = 'thermostat_heat_set_point_status'
LEAK_DETECTOR_ANNOUNCE = 'leak_detector_announce'
ASSIGN_TO_COMPANION_GROUP = 'assign_to_companion_group'
SET_SPRINKLER_PROGRAM = 'set_sprinkler_program'
SPRINKLER_GET_PROGRAM_RESPONSE = 'sprinkler_get_program_response'
IO_SET_SENSOR_NOMINAL_VALUE = 'io_set_sensor_nominal_value'
IO_ALARM_DATA_RESPONSE = 'io_alarm_data_response'
POOL_SET_DEVICE_TEMPERATURE = 'pool_set_device_temperature'
POOL_SET_DEVICE_HYSTERESIS = 'pool_set_device_hysteresis'
THERMOSTAT_ZONE_TEMPERATURE_UP = 'thermostat_zone_temperature_up'
THERMOSTAT_ZONE_TEMPERATURE_DOWN = 'thermostat_zone_temperature_down'
THERMOSTAT_SET_ZONE_HEAT_SETPOINT = 'thermostat_set_zone_heat_setpoint'
THERMOSTAT_SET_ZONE_COOL_SETPOINT = 'thermostat_set_zone_cool_setpoint'