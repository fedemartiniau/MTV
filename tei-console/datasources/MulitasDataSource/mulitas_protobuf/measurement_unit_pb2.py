# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: measurement-unit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='measurement-unit.proto',
  package='measurement.unit',
  syntax='proto2',
  serialized_pb=_b('\n\x16measurement-unit.proto\x12\x10measurement.unit*\xda\x13\n\x04Unit\x12\r\n\tUnit_NONE\x10\x00\x12\x0f\n\x0bUnit_AMPERE\x10\x01\x12\x12\n\x0eUnit_BECQUEREL\x10\x02\x12\x0c\n\x08Unit_BIT\x10\x03\x12\x10\n\x0cUnit_CANDELA\x10\x04\x12\x10\n\x0cUnit_CELCIUS\x10\x05\x12\x10\n\x0cUnit_COULOMB\x10\x06\x12\x14\n\x10Unit_CUBIC_METER\x10\x07\x12\x0e\n\nUnit_FARAD\x10\x08\x12\r\n\tUnit_GRAY\x10\t\x12\x0e\n\nUnit_HENRY\x10\n\x12\x0e\n\nUnit_HERTZ\x10\x0b\x12\x0e\n\nUnit_JOULE\x10\x0c\x12\x0e\n\nUnit_KATAL\x10\r\x12\x0f\n\x0bUnit_KELVIN\x10\x0e\x12\x11\n\rUnit_KILOGRAM\x10\x0f\x12\x0e\n\nUnit_LUMEN\x10\x10\x12\x0c\n\x08Unit_LUX\x10\x11\x12\x0e\n\nUnit_METER\x10\x12\x12\x19\n\x15Unit_METER_PER_SECOND\x10\x13\x12 \n\x1cUnit_METER_PER_SQUARE_SECOND\x10\x14\x12\r\n\tUnit_MOLE\x10\x15\x12\x0f\n\x0bUnit_NEWTON\x10\x16\x12\x0c\n\x08Unit_OHM\x10\x17\x12\x0f\n\x0bUnit_PASCAL\x10\x18\x12\x0f\n\x0bUnit_RADIAN\x10\x19\x12\x0f\n\x0bUnit_SECOND\x10\x1a\x12\x10\n\x0cUnit_SIEMENS\x10\x1b\x12\x10\n\x0cUnit_SIEVERT\x10\x1c\x12\x15\n\x11Unit_SQUARE_METER\x10\x1d\x12\x12\n\x0eUnit_STERADIAN\x10\x1e\x12\x0e\n\nUnit_TESLA\x10\x1f\x12\r\n\tUnit_VOLT\x10 \x12\r\n\tUnit_WATT\x10!\x12\x0e\n\nUnit_WEBER\x10\"\x12\x1b\n\x17Unit_WATT_PER_STERADIAN\x10#\x12!\n\x1dUnit_KILOGRAM_PER_CUBIC_METER\x10$\x12\x1a\n\x16Unit_RADIAN_PER_SECOND\x10%\x12!\n\x1dUnit_RADIAN_PER_SQUARE_SECOND\x10&\x12 \n\x1cUnit_SQUARE_METER_PER_SECOND\x10\'\x12\'\n#Unit_NEWTON_SECOND_PER_SQUARE_METER\x10(\x12\x17\n\x13Unit_VOLT_PER_METER\x10)\x12\x19\n\x15Unit_AMPERE_PER_METER\x10*\x12!\n\x1dUnit_CANDELA_PER_SQUARE_METER\x10+\x12\x19\n\x15Unit_JOULE_PER_KELVIN\x10,\x12\"\n\x1eUnit_JOULE_PER_KILOGRAM_KELVIN\x10-\x12\x1e\n\x1aUnit_WATT_PER_METER_KELVIN\x10.\x12\x11\n\rUnit_ANGSTROM\x10/\x12\x0c\n\x08Unit_ARE\x10\x30\x12\x1a\n\x16Unit_ASTRONOMICAL_UNIT\x10\x31\x12\x13\n\x0fUnit_ATMOSPHERE\x10\x32\x12\r\n\tUnit_ATOM\x10\x33\x12\x14\n\x10Unit_ATOMIC_MASS\x10\x34\x12\x0c\n\x08Unit_BAR\x10\x35\x12\r\n\tUnit_BYTE\x10\x36\x12\n\n\x06Unit_C\x10\x37\x12\x17\n\x13Unit_COMPUTER_POINT\x10\x38\x12\x13\n\x0fUnit_CUBIC_INCH\x10\x39\x12\x0e\n\nUnit_CURIE\x10:\x12\x0c\n\x08Unit_DAY\x10;\x12\x14\n\x10Unit_DAY_SIDERAL\x10<\x12\x10\n\x0cUnit_DECIBEL\x10=\x12\x15\n\x11Unit_DEGREE_ANGLE\x10>\x12\r\n\tUnit_DYNE\x10?\x12\n\n\x06Unit_E\x10@\x12\x16\n\x12Unit_ELECTRON_MASS\x10\x41\x12\x16\n\x12Unit_ELECTRON_VOLT\x10\x42\x12\x0c\n\x08Unit_ERG\x10\x43\x12\x13\n\x0fUnit_FAHRENHEIT\x10\x44\x12\x10\n\x0cUnit_FARADAY\x10\x45\x12\r\n\tUnit_FOOT\x10\x46\x12\x17\n\x13Unit_FOOT_SURVEY_US\x10G\x12\x11\n\rUnit_FRANKLIN\x10H\x12\n\n\x06Unit_G\x10I\x12\x16\n\x12Unit_GALLON_DRY_US\x10J\x12\x12\n\x0eUnit_GALLON_UK\x10K\x12\x0e\n\nUnit_GAUSS\x10L\x12\x10\n\x0cUnit_GILBERT\x10M\x12\x0e\n\nUnit_GRADE\x10N\x12\x10\n\x0cUnit_HECTARE\x10O\x12\x13\n\x0fUnit_HORSEPOWER\x10P\x12\r\n\tUnit_HOUR\x10Q\x12\r\n\tUnit_INCH\x10R\x12\x18\n\x14Unit_INCH_OF_MERCURY\x10S\x12\x17\n\x13Unit_KILOGRAM_FORCE\x10T\x12\x1c\n\x18Unit_KILOMETERS_PER_HOUR\x10U\x12\r\n\tUnit_KNOT\x10V\x12\x10\n\x0cUnit_LAMBERT\x10W\x12\x13\n\x0fUnit_LIGHT_YEAR\x10X\x12\x0e\n\nUnit_LITER\x10Y\x12\r\n\tUnit_MACH\x10Z\x12\x10\n\x0cUnit_MAXWELL\x10[\x12\x13\n\x0fUnit_METRIC_TON\x10\\\x12\r\n\tUnit_MILE\x10]\x12\x17\n\x13Unit_MILES_PER_HOUR\x10^\x12 \n\x1cUnit_MILILLIMETER_OF_MERCURY\x10_\x12\x0f\n\x0bUnit_MINUTE\x10`\x12\x15\n\x11Unit_MINUTE_ANGLE\x10\x61\x12\x0e\n\nUnit_MONTH\x10\x62\x12\x16\n\x12Unit_NAUTICAL_MILE\x10\x63\x12\x0e\n\nUnit_OCTET\x10\x64\x12\x0e\n\nUnit_OUNCE\x10\x65\x12\x18\n\x14Unit_OUNCE_LIQUID_UK\x10\x66\x12\x18\n\x14Unit_OUNCE_LIQUID_US\x10g\x12\x0f\n\x0bUnit_PARSEC\x10h\x12\x10\n\x0cUnit_PERCENT\x10i\x12\x0e\n\nUnit_PIXEL\x10j\x12\x0e\n\nUnit_POINT\x10k\x12\x0e\n\nUnit_POISE\x10l\x12\x0e\n\nUnit_POUND\x10m\x12\x14\n\x10Unit_POUND_FORCE\x10n\x12\x0c\n\x08Unit_RAD\x10o\x12\x0f\n\x0bUnit_RAKINE\x10p\x12\x0c\n\x08Unit_REM\x10q\x12\x14\n\x0fUnit_REVOLUTION\x10\xda\x08\x12\x11\n\rUnit_ROENTGEN\x10s\x12\x13\n\x0fUnit_RUTHERFORD\x10t\x12\x15\n\x11Unit_SECOND_ANGLE\x10u\x12\x0f\n\x0bUnit_SPHERE\x10v\x12\x0e\n\nUnit_STOKE\x10w\x12\x0f\n\x0bUnit_TON_UK\x10x\x12\x0f\n\x0bUnit_TON_US\x10y\x12\r\n\tUnit_WEEK\x10z\x12\r\n\tUnit_YARD\x10{\x12\r\n\tUnit_YEAR\x10|\x12\x16\n\x12Unit_YEAR_CALENDAR\x10}\x12\x15\n\x11Unit_YEAR_SIDERAL\x10~*\xcd\x03\n\nUnitPrefix\x12\x13\n\x0fUnitPrefix_NONE\x10\x00\x12\x14\n\x10UnitPrefix_YOCTO\x10\x01\x12\x14\n\x10UnitPrefix_ZEPTO\x10\x02\x12\x13\n\x0fUnitPrefix_ATTO\x10\x03\x12\x14\n\x10UnitPrefix_FEMTO\x10\x04\x12\x13\n\x0fUnitPrefix_PICO\x10\x05\x12\x13\n\x0fUnitPrefix_NANO\x10\x06\x12\x14\n\x10UnitPrefix_MICRO\x10\x07\x12\x14\n\x10UnitPrefix_MILLI\x10\x08\x12\x14\n\x10UnitPrefix_CENTI\x10\t\x12\x13\n\x0fUnitPrefix_DECI\x10\n\x12\x13\n\x0fUnitPrefix_DECA\x10\x0b\x12\x14\n\x10UnitPrefix_HECTO\x10\x0c\x12\x13\n\x0fUnitPrefix_KILO\x10\r\x12\x13\n\x0fUnitPrefix_MEGA\x10\x0e\x12\x13\n\x0fUnitPrefix_GIGA\x10\x0f\x12\x13\n\x0fUnitPrefix_TERA\x10\x10\x12\x13\n\x0fUnitPrefix_PETA\x10\x11\x12\x12\n\x0eUnitPrefix_EXA\x10\x12\x12\x14\n\x10UnitPrefix_ZETTA\x10\x13\x12\x14\n\x10UnitPrefix_YOTTA\x10\x14\x42/\n-com.invap.mulitas.serialization.impl.protobuf')
)

_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='measurement.unit.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unit_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_AMPERE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_BECQUEREL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_BIT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CANDELA', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CELCIUS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_COULOMB', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CUBIC_METER', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FARAD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GRAY', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_HENRY', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_HERTZ', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_JOULE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KATAL', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KELVIN', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KILOGRAM', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_LUMEN', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_LUX', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_METER', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_METER_PER_SECOND', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_METER_PER_SQUARE_SECOND', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MOLE', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_NEWTON', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_OHM', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_PASCAL', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RADIAN', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SECOND', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SIEMENS', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SIEVERT', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SQUARE_METER', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_STERADIAN', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_TESLA', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_VOLT', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_WATT', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_WEBER', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_WATT_PER_STERADIAN', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KILOGRAM_PER_CUBIC_METER', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RADIAN_PER_SECOND', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RADIAN_PER_SQUARE_SECOND', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SQUARE_METER_PER_SECOND', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_NEWTON_SECOND_PER_SQUARE_METER', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_VOLT_PER_METER', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_AMPERE_PER_METER', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CANDELA_PER_SQUARE_METER', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_JOULE_PER_KELVIN', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_JOULE_PER_KILOGRAM_KELVIN', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_WATT_PER_METER_KELVIN', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ANGSTROM', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ARE', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ASTRONOMICAL_UNIT', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ATMOSPHERE', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ATOM', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ATOMIC_MASS', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_BAR', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_BYTE', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_C', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_COMPUTER_POINT', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CUBIC_INCH', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_CURIE', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_DAY', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_DAY_SIDERAL', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_DECIBEL', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_DEGREE_ANGLE', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_DYNE', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_E', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ELECTRON_MASS', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ELECTRON_VOLT', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ERG', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FAHRENHEIT', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FARADAY', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FOOT', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FOOT_SURVEY_US', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_FRANKLIN', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_G', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GALLON_DRY_US', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GALLON_UK', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GAUSS', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GILBERT', index=77, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_GRADE', index=78, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_HECTARE', index=79, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_HORSEPOWER', index=80, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_HOUR', index=81, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_INCH', index=82, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_INCH_OF_MERCURY', index=83, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KILOGRAM_FORCE', index=84, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KILOMETERS_PER_HOUR', index=85, number=85,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_KNOT', index=86, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_LAMBERT', index=87, number=87,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_LIGHT_YEAR', index=88, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_LITER', index=89, number=89,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MACH', index=90, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MAXWELL', index=91, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_METRIC_TON', index=92, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MILE', index=93, number=93,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MILES_PER_HOUR', index=94, number=94,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MILILLIMETER_OF_MERCURY', index=95, number=95,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MINUTE', index=96, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MINUTE_ANGLE', index=97, number=97,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_MONTH', index=98, number=98,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_NAUTICAL_MILE', index=99, number=99,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_OCTET', index=100, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_OUNCE', index=101, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_OUNCE_LIQUID_UK', index=102, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_OUNCE_LIQUID_US', index=103, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_PARSEC', index=104, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_PERCENT', index=105, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_PIXEL', index=106, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_POINT', index=107, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_POISE', index=108, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_POUND', index=109, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_POUND_FORCE', index=110, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RAD', index=111, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RAKINE', index=112, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_REM', index=113, number=113,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_REVOLUTION', index=114, number=1114,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_ROENTGEN', index=115, number=115,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_RUTHERFORD', index=116, number=116,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SECOND_ANGLE', index=117, number=117,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_SPHERE', index=118, number=118,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_STOKE', index=119, number=119,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_TON_UK', index=120, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_TON_US', index=121, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_WEEK', index=122, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_YARD', index=123, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_YEAR', index=124, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_YEAR_CALENDAR', index=125, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unit_YEAR_SIDERAL', index=126, number=126,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=45,
  serialized_end=2567,
)
_sym_db.RegisterEnumDescriptor(_UNIT)

Unit = enum_type_wrapper.EnumTypeWrapper(_UNIT)
_UNITPREFIX = _descriptor.EnumDescriptor(
  name='UnitPrefix',
  full_name='measurement.unit.UnitPrefix',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_YOCTO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_ZEPTO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_ATTO', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_FEMTO', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_PICO', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_NANO', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_MICRO', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_MILLI', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_CENTI', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_DECI', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_DECA', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_HECTO', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_KILO', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_MEGA', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_GIGA', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_TERA', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_PETA', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_EXA', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_ZETTA', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnitPrefix_YOTTA', index=20, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2570,
  serialized_end=3031,
)
_sym_db.RegisterEnumDescriptor(_UNITPREFIX)

UnitPrefix = enum_type_wrapper.EnumTypeWrapper(_UNITPREFIX)
Unit_NONE = 0
Unit_AMPERE = 1
Unit_BECQUEREL = 2
Unit_BIT = 3
Unit_CANDELA = 4
Unit_CELCIUS = 5
Unit_COULOMB = 6
Unit_CUBIC_METER = 7
Unit_FARAD = 8
Unit_GRAY = 9
Unit_HENRY = 10
Unit_HERTZ = 11
Unit_JOULE = 12
Unit_KATAL = 13
Unit_KELVIN = 14
Unit_KILOGRAM = 15
Unit_LUMEN = 16
Unit_LUX = 17
Unit_METER = 18
Unit_METER_PER_SECOND = 19
Unit_METER_PER_SQUARE_SECOND = 20
Unit_MOLE = 21
Unit_NEWTON = 22
Unit_OHM = 23
Unit_PASCAL = 24
Unit_RADIAN = 25
Unit_SECOND = 26
Unit_SIEMENS = 27
Unit_SIEVERT = 28
Unit_SQUARE_METER = 29
Unit_STERADIAN = 30
Unit_TESLA = 31
Unit_VOLT = 32
Unit_WATT = 33
Unit_WEBER = 34
Unit_WATT_PER_STERADIAN = 35
Unit_KILOGRAM_PER_CUBIC_METER = 36
Unit_RADIAN_PER_SECOND = 37
Unit_RADIAN_PER_SQUARE_SECOND = 38
Unit_SQUARE_METER_PER_SECOND = 39
Unit_NEWTON_SECOND_PER_SQUARE_METER = 40
Unit_VOLT_PER_METER = 41
Unit_AMPERE_PER_METER = 42
Unit_CANDELA_PER_SQUARE_METER = 43
Unit_JOULE_PER_KELVIN = 44
Unit_JOULE_PER_KILOGRAM_KELVIN = 45
Unit_WATT_PER_METER_KELVIN = 46
Unit_ANGSTROM = 47
Unit_ARE = 48
Unit_ASTRONOMICAL_UNIT = 49
Unit_ATMOSPHERE = 50
Unit_ATOM = 51
Unit_ATOMIC_MASS = 52
Unit_BAR = 53
Unit_BYTE = 54
Unit_C = 55
Unit_COMPUTER_POINT = 56
Unit_CUBIC_INCH = 57
Unit_CURIE = 58
Unit_DAY = 59
Unit_DAY_SIDERAL = 60
Unit_DECIBEL = 61
Unit_DEGREE_ANGLE = 62
Unit_DYNE = 63
Unit_E = 64
Unit_ELECTRON_MASS = 65
Unit_ELECTRON_VOLT = 66
Unit_ERG = 67
Unit_FAHRENHEIT = 68
Unit_FARADAY = 69
Unit_FOOT = 70
Unit_FOOT_SURVEY_US = 71
Unit_FRANKLIN = 72
Unit_G = 73
Unit_GALLON_DRY_US = 74
Unit_GALLON_UK = 75
Unit_GAUSS = 76
Unit_GILBERT = 77
Unit_GRADE = 78
Unit_HECTARE = 79
Unit_HORSEPOWER = 80
Unit_HOUR = 81
Unit_INCH = 82
Unit_INCH_OF_MERCURY = 83
Unit_KILOGRAM_FORCE = 84
Unit_KILOMETERS_PER_HOUR = 85
Unit_KNOT = 86
Unit_LAMBERT = 87
Unit_LIGHT_YEAR = 88
Unit_LITER = 89
Unit_MACH = 90
Unit_MAXWELL = 91
Unit_METRIC_TON = 92
Unit_MILE = 93
Unit_MILES_PER_HOUR = 94
Unit_MILILLIMETER_OF_MERCURY = 95
Unit_MINUTE = 96
Unit_MINUTE_ANGLE = 97
Unit_MONTH = 98
Unit_NAUTICAL_MILE = 99
Unit_OCTET = 100
Unit_OUNCE = 101
Unit_OUNCE_LIQUID_UK = 102
Unit_OUNCE_LIQUID_US = 103
Unit_PARSEC = 104
Unit_PERCENT = 105
Unit_PIXEL = 106
Unit_POINT = 107
Unit_POISE = 108
Unit_POUND = 109
Unit_POUND_FORCE = 110
Unit_RAD = 111
Unit_RAKINE = 112
Unit_REM = 113
Unit_REVOLUTION = 1114
Unit_ROENTGEN = 115
Unit_RUTHERFORD = 116
Unit_SECOND_ANGLE = 117
Unit_SPHERE = 118
Unit_STOKE = 119
Unit_TON_UK = 120
Unit_TON_US = 121
Unit_WEEK = 122
Unit_YARD = 123
Unit_YEAR = 124
Unit_YEAR_CALENDAR = 125
Unit_YEAR_SIDERAL = 126
UnitPrefix_NONE = 0
UnitPrefix_YOCTO = 1
UnitPrefix_ZEPTO = 2
UnitPrefix_ATTO = 3
UnitPrefix_FEMTO = 4
UnitPrefix_PICO = 5
UnitPrefix_NANO = 6
UnitPrefix_MICRO = 7
UnitPrefix_MILLI = 8
UnitPrefix_CENTI = 9
UnitPrefix_DECI = 10
UnitPrefix_DECA = 11
UnitPrefix_HECTO = 12
UnitPrefix_KILO = 13
UnitPrefix_MEGA = 14
UnitPrefix_GIGA = 15
UnitPrefix_TERA = 16
UnitPrefix_PETA = 17
UnitPrefix_EXA = 18
UnitPrefix_ZETTA = 19
UnitPrefix_YOTTA = 20


DESCRIPTOR.enum_types_by_name['Unit'] = _UNIT
DESCRIPTOR.enum_types_by_name['UnitPrefix'] = _UNITPREFIX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n-com.invap.mulitas.serialization.impl.protobuf'))
# @@protoc_insertion_point(module_scope)